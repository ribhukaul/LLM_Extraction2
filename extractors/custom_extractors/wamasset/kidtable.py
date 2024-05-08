import os

from extractors.general_extractors.llm_functions import general_table_inspection
from extractors.models import Models
from extractors.general_extractors.custom_extractors.kid.kid_extractor import KidExtractor
from extractors.general_extractors.utils import upload_df_as_excel
from extractors.general_extractors.custom_extractors.kid.kid_utils import clean_response_regex


class WamAssetKidFeesExtractor(KidExtractor):
    def __init__(self, doc_path, predefined_language=False) -> None:
        self.tenant = "wamasset"
        self.extractor = "kidasset"
        self.doc_path = doc_path
        super().__init__(doc_path, "it", tenant=self.tenant, extractor=self.extractor)
    
    def get_tables(self):
        """calc table extractor, it extracts the three tables from the document asynchronously

        Returns:
            dict([pandas.dataframe]): tables as dataframe
        """
        try:
            costi_ingresso_table,_ = self._extract_table("costi_ingresso", black_list_pages=[0])
            costi_gestione_table,_ = self._extract_table("costi_gestione")
  
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

    def extract_transaction_costs(self, table):
        try:
            
            extract_transaction_cost_schema = self.extraction_config['tag'].get('costi_gestione')
            table = upload_df_as_excel(table)
            extraction = dict()
            extraction = general_table_inspection(
                table,
                extract_transaction_cost_schema,
                self.file_id,
                add_text="estrai il valore % dei costi correnti e dei costi di transazione",
            )
            extraction = clean_response_regex("costi_gestione_wamasset", self.language, extraction)
        except Exception as error:
            print("extract management costs error" + repr(error))
            error_list = ["commissione_gestione", "commissione_transazione", "commissione_performance"]
            extraction = {key: (extraction[key] if extraction.get(key) is not None else "ERROR") for key in error_list}

        return extraction
    
    def extract_middle_costs(self, table):
        try:
            extract_middle_cost_schema = self.extraction_config['tag'].get('costi_ingresso')
            table = upload_df_as_excel(table)
            extraction = general_table_inspection(
                table,
                extract_middle_cost_schema,
                self.file_id,
                add_text="l'Estrazione deve dare i soli numeri come risposta, Estrai i valori % ed i diritti fissi in €")
            extraction = clean_response_regex("costi_ingresso_wamasset", self.language, extraction)
        except Exception as error:
            print("extract middle costs error" + repr(error))
            error_list = ["costi_ingresso", "costi_uscita","costiuscita_dirittifissi","costiingresso_dirittifissi"]
            # Initialize a default error structure for the extraction
            extraction = {key: "ERROR" for key in error_list}

        return extraction
    
    def extract_picpac(self):
        try:
            extract_picpac_schema = self.extraction_config['tag'].get('picpac')
            n = int(len(self.text[0].page_content)/3)
            first_page = self.text[0].page_content[:n]
            extraction = Models.tag(first_page, extract_picpac_schema, self.file_id)
        except Exception as error:
            print("extract picpac error" + repr(error))
            extraction = {"picpac": "ERROR"}

        return extraction

    def process(self):
        # first stage, basic info
        try:
            functions_parameters = {
                "tables": {"function": self.get_tables},
                "basic_information": {"function":self.extract_general_data},
                "picpac" : {"function": self.extract_picpac},
            }
            result = self.threader(functions_parameters)
            table = result["tables"]
            basic_information = result["basic_information"]
            picpac = result["picpac"]
        
        except Exception as error:
            print("first stage error" + repr(error))
        
        # second stage:
        try:

            functions_parameters = {
                "cost": { "function": self.extract_middle_costs, "args":{"table": table["costi_ingresso"].iloc[:, :2]}},
                "transaction": {"function": self.extract_transaction_costs, "args":{"table": table["costi_gestione"]}},
            }
        
            result = self.threader(functions_parameters)
            cost = result["cost"]
            gestione = result["transaction"]
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


        


         