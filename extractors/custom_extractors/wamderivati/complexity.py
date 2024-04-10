

from extractors.models import Models
from extractors.general_extractors.extractor import Extractor
#from extractors.configs.extraction_config.tags.wamderivati.complexity_tags import PydanticSchema_unicredit_noLangChain
import os
from langchain_core.prompts import PromptTemplate
from .complexity_custom.setting.column_config import column_dict, columns_to_clean, columns_to_date_convert, new_df_renaming

import pandas as pd
from .complexity_custom.setting.functions import get_new_column_name, truncate, clean_value, convert_date
from .complexity_custom.postprocessing.dataintegration import df_dataintegration


class WamDerivatiComplexity(Extractor):

    def __init__(self, doc_path, predefined_language='it'):
        self.tenant = "wamderivati"
        self.extractor = "complexity"
        super().__init__(doc_path, predefined_language, tenant=self.tenant, extractor=self.extractor)

    
    def process(self):


        system_message = self.extraction_config["prompt"]["complexity_system"]
        human_message =  self.extraction_config["prompt"]["complexity_human"]

        complete_prompt = system_message + human_message

        prompt_kid = PromptTemplate(input_variables=["input"], template=complete_prompt)
        response = Models.general_extract(self.doc_path, "gpt-4-turbo", prompt=prompt_kid, input=self.text)
        complexity_schema = self.extraction_config["tag"]["complexity"]
        tags  = Models.tag(response, complexity_schema, self.file_id)

        df_tags = pd.DataFrame.from_dict([dict(tags)])
        df_guesses = df_tags.rename(columns=lambda x: get_new_column_name(column_dict, x))
        df_guesses = df_guesses.applymap(truncate)
        df_guesses = df_guesses.replace("'", " ", regex=True)

        df_guesses[columns_to_clean] = df_guesses[columns_to_clean].applymap(clean_value)
        df_guesses[columns_to_date_convert] = df_guesses[columns_to_date_convert].applymap(convert_date)

        df_final = df_dataintegration(df_guesses)
        # get list of column names
        # rename df columns 
        df_final_renamed = df_final.rename(columns=new_df_renaming)
        # from df to dict
        tags = df_final_renamed.to_dict(orient="records")[0]
        

        api_costs = self._process_costs()

        filename = os.path.splitext(os.path.basename(self.doc_path))[0]
        complete_results  = {
                "file_name": filename,
                **dict(tags),
                "api_costs": api_costs
            }

        formatted_output = self.create_output(complete_results)

        Models.clear_resources_file(filename)

        return formatted_output

