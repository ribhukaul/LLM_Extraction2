import os

from extractors.models import Models
from extractors.general_extractors.custom_extractors.kid.kid_extractor import KidExtractor
from extractors.general_extractors.utils import upload_df_as_excel
from extractors.general_extractors.custom_extractors.kid.kid_utils import clean_response_regex
from extractors.azure.document_intelligence import get_tables_from_doc
from langchain_core.prompts import PromptTemplate

class WamAssetKidFeesExtractor(KidExtractor):
    
    def __init__(self, doc_path) -> None:
        self.tenant = "wamasset"
        self.extractor = "kidasset"
        self.doc_path = doc_path
        super().__init__(doc_path, tenant=self.tenant, extractor=self.extractor)

        # Som PDFs are scanned or are badly uploaded
        self.adjust_pages()
    
    def adjust_pages(self):
        
        for i, _ in enumerate(self.text[:3]):
            pag=i+1
            tables, raw_data = get_tables_from_doc(self.doc_path, specific_pages=pag, language=self.language, high_res=False)
            self.di_tables_pages[str(i)], self.raw_data_pages[str(i)]= tables, raw_data
            self.text[i].page_content = raw_data['content']
        # For the time being, we are only interested in the first three pages
        # in the future the splitter will automatically trim the document
        self.text = self.text[:3]
            
    def get_tables(self):
        """calc table extractor, it extracts the three tables from the document asynchronously

        Returns:
            dict([pandas.dataframe]): tables as dataframe
        """
        try:
            costi_ingresso_table,_ = self._extract_table("costi_ingresso", black_list_pages=[0])
            costi_gestione_table,_ = self._extract_table("costi_gestione", black_list_pages=[0])
  
        except Exception as error:
            print("calc table error" + repr(error))
            error_list = [costi_ingresso_table, costi_gestione_table]
            for i, key in enumerate(error_list):
                if not key:
                    error_list[i] = dict([("ERROR", "ERROR")])

        return {
            "costi_ingresso": costi_ingresso_table,
            "costi_gestione": costi_gestione_table,
        }

    def extract_naming(self):

        try:
            naming_schema = self.extraction_config['tag'].get('naming')
            naming_prompt = self.extraction_config['prompt'].get('naming')
            prompt = naming_prompt.format(self.text[0].page_content[:700])
            extraction = Models.tag(prompt, naming_schema, self.file_id, model="gpt-3.5-turbo")
        except Exception as error:
            print("extract naming error" + repr(error))
            extraction = {"nome_fondo": "ERROR"}

        return extraction

    def extract_transaction_costs(self, table):
        try:
            # Prompt creation
            transaction_cost_schema = self.extraction_config['tag'].get('costi_gestione')
            transaction_cost_prompt = self.extraction_config['prompt'].get('costi_gestione')
            loaded_table = upload_df_as_excel(table)
            prompt = transaction_cost_prompt.format(loaded_table)
            # Extraction
            extract = Models.tag(prompt, transaction_cost_schema, self.file_id)
            extraction = clean_response_regex("costi_gestione_wamasset", self.language, extract)
        except Exception as error:
            print("extract management costs error" + repr(error))
            error_list = [k for k in transaction_cost_schema.schema()['properties'].keys()]
            extraction = {key: (extraction[key] if extraction.get(key) is not None else "ERROR") for key in error_list}

        return extraction
    
    def extract_middle_costs(self, table):
        try:
            # Prompt creation
            middle_cost_schema = self.extraction_config['tag'].get('costi_ingresso')
            middle_cost_prompt = self.extraction_config['prompt'].get('costi_ingresso')
            loaded_table = upload_df_as_excel(table)
            prompt = middle_cost_prompt.format(loaded_table)
            # Extraction
            extract = Models.tag(prompt, middle_cost_schema, self.file_id)
            extraction = clean_response_regex("costi_ingresso_wamasset", self.language, extract)
        except Exception as error:
            print("extract middle costs error" + repr(error))
            error_list = [k for k in middle_cost_schema.schema()['properties'].keys()]
            # Initialize a default error structure for the extraction
            extraction = {key: "ERROR" for key in error_list}

        return extraction
    
    def extract_picpac(self):
        try:
            if self.language == "en":
                extraction = {"picpac": "-"}
            else:    
                extract_picpac_schema = self.extraction_config['tag'].get('picpac')
                n = int(len(self.text[0].page_content)/3)
                first_page = self.text[0].page_content[:n]
                extraction = Models.tag(first_page, extract_picpac_schema, self.file_id)
        except Exception as error:
            print("extract picpac error" + repr(error))
            extraction = {"picpac": "ERROR"}

        return extraction

    
    def extract_strategy(self):
        try:
            strategy_prompt = self.extraction_config['prompt'].get('strategy')
            complete_strategy_prompt = PromptTemplate(input_variables=["input"], template=strategy_prompt)
            #prompt = strategy_prompt.format(self.text[0].page_content)
            extraction = Models.general_extract(self.file_id, 'gpt-3.5-turbo', complete_strategy_prompt, self.text[0].page_content)
            extraction = {"strategia_fondo": extraction}
        except Exception as error:
            print("extract strategy error" + repr(error))
            extraction = {"strategia_fondo": "ERROR"}

        return extraction
    
    def process(self):
        # first stage, basic info
        try:
            functions_parameters = {
                "tables": {"function": self.get_tables},
                "basic_information": {"function":self.extract_general_data},
                "naming": {"function": self.extract_naming},
                "picpac" : {"function": self.extract_picpac},
                "strategy": {"function": self.extract_strategy}
            }
            result = self.threader(functions_parameters)
            table = result["tables"]
            basic_information = result["basic_information"]
            picpac = result["picpac"]
            naming = result["naming"]
            strategia_fondo = result["strategy"]
        
        except Exception as error:
            print("first stage error" + repr(error))
        
        # second stage:
        try:

            functions_parameters = {
                "cost": { "function": self.extract_middle_costs, "args":{"table": table["costi_ingresso"].iloc[:, :-1]}},
                "transaction": {"function": self.extract_transaction_costs, "args":{"table": table["costi_gestione"]}},
                "riy": {"function": self.extract_riy_small},
            }
        
            result = self.threader(functions_parameters)
            cost = result["cost"]
            gestione = result["transaction"]
            riy = result["riy"]
        except Exception as error:
            print("second stage error" + repr(error))

        
        try:
            filename = os.path.splitext(os.path.basename(self.doc_path))[0]
            api_costs = self._process_costs()
            complete_resutls = {
                "file_name": filename,
                **dict(basic_information),
                **dict(cost),
                **dict(gestione),
                **dict(picpac),
                **dict(strategia_fondo),
                **dict(riy),
                **dict(naming),
                "api_costs": api_costs,
            }
            # Format output
            formatted_output = self.create_output(complete_resutls)
            
        except Exception as error:
            print("dictionary error" + repr(error))
            filename = os.path.splitext(os.path.basename(self.doc_path))[0]
            formatted_output = dict([(filename), dict()])

        print(formatted_output)
        Models.clear_resources_file(filename)

        return formatted_output


        


         