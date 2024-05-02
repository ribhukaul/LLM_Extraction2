from extractors.models import Models
from extractors.general_extractors.custom_extractors.kid.kid_extractor import KidExtractor
import os
from  langchain.schema import Document
import json
from typing import Iterable
class WamCGA(KidExtractor):

    def __init__(self, doc_path) -> None:
        self.tenant = 'waminsurance'
        self.extractor = 'cga'
        self.doc_path = doc_path
        super().__init__(doc_path, "it", tenant=self.tenant, extractor=self.extractor)


    def load_docs_from_jsonl(self, file_path)->Iterable[Document]:
        array = []
        with open(file_path, 'r') as jsonl_file:
            for line in jsonl_file:
                data = json.loads(line)
                obj = Document(**data)
                array.append(obj)
        return array
    

    def select_words_around_word(self,text,  word, before_words, after_words):
        """Selects a specified number of words before and after each occurrence in a list of indices.

        Args:
            text: The string to extract words from.
            indices: A list of indices where the search string is found.
            before_words: The number of words to select before each occurrence.
            after_words: The number of words to select after each occurrence.

        Returns:
            A list of strings, each containing the specified number of words before and after a given index.
        """

        text = text.replace(word, ' ' + word + ' ')
        if ' ' in word:
            text = text.replace('  ', ' ')
      
        start=0
        sections =[]
        while True:
            index = text.find(word, start)
            if index == -1:
                break
            start = index + len(word)

            forward = text[index:].split()
            backward = text[:index].split()
            backward_str = ['']
            foreward_str = [word]
            if before_words != 0:
                backward_str = backward[-before_words:]
            if after_words != 0:
                foreward_str = forward[:after_words]

            complete = backward_str + foreward_str

            sections.append(' '.join(complete))

        return sections


    def get_section_with_text(self, word, backward_words=10, forward_words=10):
   
        sections = []
        for t in self.text:
            t = t.page_content.lower()
   
            section = self.select_words_around_word(t, word, backward_words, forward_words)

            sections.extend(section)
           
        return sections
    
    def get_vita_intera(self):

        vita_intera = self.text[0].page_content.lower().find('vita intera') != -1
        
        if not vita_intera:
            sections = self.get_section_with_text('durata', forward_words=20, backward_words=0)
            durata_schema = self.extraction_config['tag']['durata']

            max_idx = min(10, len(sections))

            prompt = """condierando ispezzoni di un documento, chiarisci quanto sia la durata del contratto in anni
            potrebbe essere necessario specificare un range di anni:
            SPEZZONI:
            {}
            """.format(sections[2:max_idx])

            durata = Models.tag(prompt, durata_schema, self.file_id)

        result = {'tariffa': 'VITA INTERA' if vita_intera else 'DURATA PREFISSATA',
                  'durata': 'Vita sottoscrittore' if vita_intera else durata.durata}
   
        return result
    
    def get_premium_type(self):

        sections_unico = self.get_section_with_text('premio unico', forward_words=10, backward_words=5)
        prompt  = """condierando ispezzoni di un documento, chiarisci se il premio è unicco o meno:
        Spezzone:
        {}
        """.format(sections_unico)
        is_premio_unico = self.extraction_config['tag']['is_unico']
        premio_unico =Models.tag(prompt, is_premio_unico, self.file_id)

        # Section for recurrent premiums
        sections_ricorrenti_1 = self.get_section_with_text('premi unici ricorrenti', forward_words=10, backward_words=5)
        sections_ricorrenti_2 = self.get_section_with_text('premi ricorrenti', forward_words=10, backward_words=0)
        is_rec = len(sections_ricorrenti_1) + len(sections_ricorrenti_2) != 0
        #section_premio_annuo = self.get_section_with_text('premio annuo', forward_words=15, backward_words=10)
        if is_rec:
            prompt = """condierando degli spezzoni di un documento, chiarisci se il premio è ricorrente(se non è ricorrente 
            allora non è annuo, se è riocorrente allora può essere annuo o meno)
            RICORDA!!
            - PREMI RICORRENTI/ANNUI PER ASSICURAZIONI facoltative/aggiuntive non sono da considerarsi
            Spezzone ricorrenti:
            {} 
            {}
            """.format(sections_ricorrenti_1, sections_ricorrenti_2)#, section_premio_annuo)

            is_premio_ricorrente = self.extraction_config['tag']['is_premio_ricorrente']

            recurrent_premium = Models.tag(prompt, is_premio_ricorrente, self.file_id)
            recurrent_premium = 'true' if recurrent_premium.is_premio_ricorrente else 'false'

        reults = {'unico': 'true' if premio_unico.is_unico else 'false',
                  'ricorrente': 'false' if not is_rec else recurrent_premium
                  }#'annuo': recurrent_premium.is_premio_annuo}
        
        return reults


    def process(self):
        """main processor in different phases, first phases extracts the tables and general information,
        and target market, second phase extracts the rest of the fields.

        Returns:
            dict(filename,dict()): dictionary containing the results for the file
        """
        # FIRST STAGE: get tables and general information
        try:
            #self.get_doc_markdown()

            #self.text_azure = self.load_docs_from_jsonl(self.doc_path.replace('.pdf', '.json'))
            vita_intera = self.get_vita_intera()#db_md)

            premium_type = self.get_premium_type()
            #total = {, **premium_type}#, **boundaries}**vita_intera, 
            api_costs = self._process_costs()
            file_name = os.path.splitext(os.path.basename(self.doc_path))[0]
            complete_results  = {
                "file_name": file_name,
                **dict(vita_intera),
                **premium_type,
                "api_costs": api_costs
            }
            formatted_output = self.create_output(complete_results)
            Models.clear_resources_file(file_name)
        except Exception as error:
            print("Error in process: " + repr(error))

        return formatted_output

