import os
import pandas as pd
import re
from extractors.models import Models
from extractors.general_extractors.custom_extractors.kid.kid_extractor import KidExtractor
from extractors.general_extractors.llm_functions import llm_extraction_and_tag, tag_only

from extractors.general_extractors.config.prompt_config import prompts, table_schemas, word_representation
class WamInsuranceKidModuleExtractor(KidExtractor):

    def __init__(self, doc_path) -> None:
        self.tenant = "waminsurance"
        self.extractor = "kidmodule"
        self.doc_path = doc_path
        super().__init__(doc_path, "it", tenant=self.tenant, extractor=self.extractor)

    
    def sottostante_extractor(self,isin):
        sottostante = dict()
        try:
            if isin != '-':
                sottostante['nome_sottostante'] = isin
                sottostante['tipo_gestione'] = "Fondo Esterno"
            else:
                sottostante_prompt = self.extraction_config['prompt']["sottostante"]
                sottostante_schema = self.extraction_config['tag']["sottostante"]
                sottostante = dict(llm_extraction_and_tag(self.text, sottostante_prompt,sottostante_schema, self.file_id,0))
            
            if sottostante.get('nome_sottostante')=='not found':
                pattern = r"Gestione Separata\s*['\"]?([A-Z][\w\s]*)['\"]?"
                first_page_text = str(self.text[0]) 
                matches = re.findall(pattern, first_page_text)
                if matches:
                    valid_name = matches[0].strip().strip('\'"')
                    sottostante['nome_sottostante'] = valid_name  # Captures the capital word after the keyword
            if not sottostante.get('tipo_gestione'):
                    if "Gestione Separata" in self.text:
                        sottostante['tipo_gestione'] = "Gestione Separata"
                    elif "Fondo Interno" in self.text:
                        sottostante['tipo_gestione'] = "Fondo Interno"      
        
        except Exception as error:
            print(f"Error extracting underlying asset info: {repr(error)}")

        return sottostante
    

    
        
    def process(self):
        """main processor in different phases, first phases extracts the tables and general information,
        and target market, second phase extracts the rest of the fields.

        Returns:
            dict(filename,dict()): dictionary containing the results for the file
        """
        # FIRST STAGE: get tables and general information
        try:
      
            functions_parameters = {
                "tables": {"function":self.get_tables}, 
                "basic_information": {"function":self.extract_general_data, "args":{"general_info_type":"general_info_premio"}},
                "target_market": {"function":self.extract_market},
                "isin": {"function":self.extract_isin}
                }
            results = self.threader(functions_parameters)

            tables = results["tables"]
            basic_information = results["basic_information"]
            basic_information["premio"] = "periodico" if basic_information["premio"] == 1000 else "unico"


            target_market = results["target_market"]
            isin = results["isin"]


        except Exception as error:
            print("first stage error" + repr(error))

        # SECOND STAGE: extract RIY, costs, commissions and performances
        try:
            functions_parameters = {
                "riy": {"function":self.extract_riy_small}, 
                "costs": {"function":self.extract_entryexit_costs, "args":{"table":tables["costi_ingresso"]}},
                "management_costs": {"function":self.extract_management_costs, "args": {"table":tables["costi_gestione"]}},
                "performance": {"function":self.extract_performances, "args":{"table":tables["performance"]}},
                #"sottostante": {"function": self.sottostante_extractor, "args":{"isin":isin}}
               
                }
           
            
            results = self.threader(functions_parameters)
            riy = results["riy"]
            exit_entry_costs = results["costs"]
            management_costs = results["management_costs"]
            performance = results["performance"]   
            #sottostante = results["sottostante"]
            
           

        except Exception as error:
            print("second stage error" + repr(error))

            

        try:
            # REVIEW: what name do they need?
            filename = os.path.splitext(os.path.basename(self.doc_path))[0]
            api_costs = self._process_costs()
            complete_results = {
                "file_name": filename,
                **dict(basic_information),
                **dict(performance),
                **dict(riy),
                **dict(exit_entry_costs),
                **dict(management_costs),
                **dict(target_market),
                #**sottostante,
                "api_costs": api_costs,
            }
            # Format output
            formatted_output = self.create_output(complete_results)


        except Exception as error:
            print("dictionary error" + repr(error))
            filename = os.path.splitext(os.path.basename(self.doc_path))[0]
            formatted_output = dict([(filename), dict()])

        #print(dict(underlying))
        Models.clear_resources_file(filename)

        return formatted_output

