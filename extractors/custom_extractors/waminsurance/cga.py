import os

from extractors.models import Models
from extractors.general_extractors.custom_extractors.kid.kid_extractor import KidExtractor
from langchain_openai import AzureOpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores.chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from  langchain.schema import Document
import json
from typing import Iterable

class WamInsuranceCGA(KidExtractor):

    def __init__(self, doc_path) -> None:
        self.tenant = 'waminsurance'
        self.extractor = 'cga'
        self.doc_path = doc_path
        super().__init__(doc_path, "it", tenant=self.tenant, extractor=self.extractor)


    def _add_metadata(self, splitted_text, metadata):
        for text in splitted_text:
            # pdate metadata dict
            text.metadata = metadata
        return splitted_text


    def save_docs_to_jsonl(self, array:Iterable[Document], file_path:str)->None:
        with open(file_path, 'w') as jsonl_file:
            for doc in array:
                jsonl_file.write(doc.json() + '\n')

    def load_docs_from_jsonl(self, file_path)->Iterable[Document]:
        array = []
        with open(file_path, 'r') as jsonl_file:
            for line in jsonl_file:
                data = json.loads(line)
                obj = Document(**data)
                array.append(obj)
        return array
        


    def get_doc_markdown(self):
            # read txt file
            from langchain_community.document_loaders import AzureAIDocumentIntelligenceLoader
            endpoint = os.environ.get("AZURE_FORM_RECOGNIZER_ENPOINT")
         
            key = os.environ.get("AZURE_FORM_RECOGNIZER_KEY")
            loader = AzureAIDocumentIntelligenceLoader(
                api_endpoint=endpoint, api_key=key, file_path=self.doc_path, api_model="prebuilt-layout", mode='markdown', api_version='2024-02-29-preview'
            )
            text = loader.load()
            #save create name changing from .pdf to .json
            json_name = self.doc_path.replace('.pdf', '.json')
            self.save_docs_to_jsonl(text, json_name)
            

 


    def get_vita_intera(self, db):
        query = "quanto dura il contratto?"
        results = db.similarity_search(query, k=2)

        prompt = """
        considerando i seguenti spezzoni di un documento, chiarisci se il contratto è a vita intera
        PEZZI DEL DOCUMENTO:
        {}
        """.format(results)

        vita_intera_tag = self.extraction_config['tag']['vita_intera']
        extraction = Models.tag(prompt, vita_intera_tag, self.file_id)

        if not extraction.is_vita_intera:
            durata_schema = self.extraction_config['tag']['durata'] 

            results = "quanto è la durata del contratto?"
            durata_chunk = db.similarity_search(results, k=2)

            prompt = """condierando il seguente spezzone di un documento, chiarisci quanto sia la durata del contratto:
            SPEZZONI:
            {}
            """.format(durata_chunk)
            durata = Models.tag(prompt, durata_schema, self.file_id)
            
        else:
            durata = None

        result = {'tariffa': 1 if extraction.is_vita_intera == 'vita intera' else 0,
                  'durata': 'NA' if durata is None else durata.durata }

        return result
    
    def premium_type(self, db):#, db_small, db_medium, db_large):
        query1 = "come e quando devo pagare, premio da versare. modalità di versamento del premio."#tipologia di premi prevede il contratto e modalità di pagamento, premio unico o ricorrente"
        #query2 = "pagamento dei premi"
        query1 = ' tipologia del premio o premio unico o ricorrente'


        found = db.similarity_search(query1, k=3)#, filter={'type': 'db_large'})
        # small = db_small.similarity_search(query1, k=2,  filter={'type': 'db_small'})
        #med = db_medium.similarity_search(query1, k=2, filter={'type': 'db_medium'})
        #big = db_large.similarity_search(query1, k=2, filter={'type': 'db_large'})
        # premium_chunk1 = db.similarity_search(query1, k=2)
        # premium_chunk_db_small = db_small.similarity_search(query1, k=2)
        # premium_chunk_db_medium = db_medium.similarity_search(query1, k=2)
        # premium_chunk_db_large = db_large.similarity_search(query1, k=2)
        # #premium_chunk2 = db.similarity_search(query2, k=2)

        premium_prompt = """ Considerando i seguenti spezzoni di un documento, quale è la tipologia di premio?
        - unico
        - periodico
        - a scelta (quando c'è esplicitamente detto che si può investire in modalità a versamento unico o modalità ricorrente)
        (somme investite in maniera integrativa non rappresentano investimenti periodici)
        (somme di denaro investite per garanzie aggiuntive non sono da considerare per la risposta)

        SPEZZONI:
        {}
        """.format(found)

        premium_tag = self.extraction_config['tag']['premium_type']
        extraction = Models.tag(premium_prompt, premium_tag, self.file_id)

        dict_sw = {
            'unico': 0,
            'periodico': 1,
            'a scelta': 2 
        }
        extraction = {'tipo_premio': dict_sw[extraction.premium_type]}
        

        return extraction
        
    def premium_boundaries(self, db):
        query = "Quando e come devo pagare? limiti di premio, inferiore e superiore (premio minimo e massimo)"
        results = db.similarity_search(query)

        prompt = """
        considerando i seguenti spezzoni di un documento, chiarisci i limiti di premio
        SPEZZONI:
        {}
        """.format(results)

        extraction = Models.tag(prompt, self.extraction_config['tag']['premium_boundaries'], self.file_id)

        return extraction

    def process(self):
        """main processor in different phases, first phases extracts the tables and general information,
        and target market, second phase extracts the rest of the fields.

        Returns:
            dict(filename,dict()): dictionary containing the results for the file
        """
        # FIRST STAGE: get tables and general information
        try:
            #self.get_doc_markdown()


            self.text_azure = self.load_docs_from_jsonl(self.doc_path.replace('.pdf', '.json'))
            
            from langchain_community.document_loaders import UnstructuredMarkdownLoader
            #loader = UnstructuredMarkdownLoader('res.txt')
            text_splitter_small = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=15)
            text_splitter_medium = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=30)
            text_splitter_large = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=45)
            markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on = [
                ("#", "Header 1"),
                ("##", "Header 2"),
                ("###", "Header 3")
            ])
            splitted_text = markdown_splitter.split_text(self.text_azure[0].page_content)

            # documents = loader.load()
            
            # documents_small = text_splitter_small.split_documents(self.text)
            # documents_medium = text_splitter_medium.split_documents(self.text)
            # documents_large = text_splitter_large.split_documents(self.text)
            # documents_small = self._add_metadata(documents_small, {"type": "db_small"})
            # documents_medium = self._add_metadata(documents_medium, {"type": "db_medium"})
            # documents_large = self._add_metadata(documents_large, {"type": "db_large"})
            #splitted_text = self._add_metadata(splitted_text)#, {"type": "maked_down_db"})

            dep_name = os.environ.get("AZURE_OPENAI_EMBEDDING_DEP_NAME")
            
            embedding = AzureOpenAIEmbeddings(azure_deployment=dep_name)
            # x = Chroma(embedding_function=embedding)
            # x.add_documents(documents_small, name="db_small")
            # x.add_documents(documents_medium, name="db_medium")
            # x.add_documents(documents_large, name="db_large")
            # x.add_documents(splitted_text, name="maked_down_db")
            db_md = Chroma.from_documents(splitted_text, embedding=embedding)
            # db_small = Chroma.from_documents(documents_small, embedding=embedding, collection_metadata={"collection_name": "db_small"})
            # db_medium = Chroma.from_documents(documents_medium, embedding=embedding, collection_metadata={"collection_name": "db_medium"})
            # db_large = Chroma.from_documents(documents_large, embedding=embedding, collection_metadata={"collection_name": "db_large"})

            vita_intera = self.get_vita_intera(db_md)
            #premium = dict(self.premium_type(db_large))
            #boundaries = dict(self.prempremium_typeium_boundaries(maked_down_db))

            db_md.delete_collection()
            # db_small.delete_collection()
            # db_medium.delete_collection()
            # db_large.delete_collection()
        
            total = {**vita_intera}#, **boundaries}**vita_intera, 
            
            return total
            # print(results)


        except Exception as error:
            print("Error in process: " + repr(error))

          
        return {}

