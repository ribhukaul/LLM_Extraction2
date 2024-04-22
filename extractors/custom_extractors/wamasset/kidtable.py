import os
from extractors.general_extractors.config.prompt_config import prompts,table_schemas,word_representation
from extractors.general_extractors.utils import select_desired_page
from extractors.models import Models
from extractors.general_extractors.custom_extractors.kid.kid_extractor import KidExtractor
from extractors.general_extractors.llm_functions import complex_table_inspection
from extractors.general_extractors.custom_extractors.kid.kid_utils import clean_response_regex
import pandas as pd

class WamassetKidTableextractor(KidExtractor):
    def __init__(self, doc_path, predefined_language=False) -> None:
        self.tenant = "wamasset"
        self.extractor = "kidasset"
        self.doc_path = doc_path
        super().__init__(doc_path, "it", tenant=self.tenant, extractor=self.extractor)
    
    


    def process(self):
        # first stage, basic info
        try:
            functions_parameters = {
                "tables": {"function": self.get_tables},
                "basic_information": {"function":self.extract_general_data},

            }
            result = self.threader(functions_parameters)
            table = result["tables"]
            basic_information = result["basic_information"]

        
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


        


         