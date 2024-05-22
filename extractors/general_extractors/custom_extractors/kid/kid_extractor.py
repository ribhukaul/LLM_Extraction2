from math import ceil
import re

from ...llm_functions import complex_table_inspection, general_table_inspection, llm_extraction, llm_extraction_and_tag
from ...extractor import Extractor
from extractors.models import Models
from extractors.general_extractors.utils import upload_df_as_excel, select_desired_page
from .kid_utils import clean_response_regex, clean_response_strips


class KidExtractor(Extractor):

    def __init__(self, doc_path, predefined_language=False, tenant='general', extractor='general') -> None:
        super().__init__(doc_path, predefined_language, tenant, extractor)


    def get_tables(self):
        """calc table extractor, it extracts the three tables from the document asynchronously

        Returns:
            dict([pandas.dataframe]): tables as dataframe
        """
        try:
            performance_table,_ = self._extract_table("performance")
            costi_ingresso_table,_ = self._extract_table("costi_ingresso", black_list_pages=[0])
            costi_gestione_table,_ = self._extract_table("costi_gestione", black_list_pages=[0])
            #riy, _ = self._extract_table("riy", black_list_pages=[0])
            
        except Exception as error:
            print("calc table error" + repr(error))
            error_list = [performance_table, costi_ingresso_table, costi_gestione_table]
            for i, key in enumerate(error_list):
                if not key:
                    error_list[i] = dict([("ERROR", "ERROR")])

        return {
            "costi_ingresso": costi_ingresso_table,
            "costi_gestione": costi_gestione_table,
            "performance": performance_table
        }

    def extract_general_data(self, general_info_type="general_info"):
        """
        Extract general data from the document. Namely RHP and SRI.


        Returns: dict(): data extracted
        """
        extraction = dict()
        try:
            # extract and clean
            general_info_prompt = self.extraction_config['prompt'][general_info_type]
            general_info_schema = self.extraction_config['tag'][general_info_type]
        
            extraction = llm_extraction_and_tag(self.text, general_info_prompt, general_info_schema, self.file_id)
            extraction = clean_response_regex("general_info", self.language, extraction)
            extraction = dict(extraction)

            # REVIEW: ISIN EXTRACTION TO BE MOVED OUTSIDE?
            isin = self.extract_isin()
            extraction.update({"isin": isin})
            if (
                "periodo_detenzione_raccomandato" in extraction
                and extraction["periodo_detenzione_raccomandato"] != "-"
                and re.search(r"\d+", extraction["periodo_detenzione_raccomandato"])
            ):

                rhp_temp = extraction["periodo_detenzione_raccomandato"]
                number = re.search(r"\d+", rhp_temp).group(0)
                if re.search(r"(?i)mesi", rhp_temp):
                    extraction["periodo_detenzione_raccomandato"] = "1"
                else:
                    extraction["periodo_detenzione_raccomandato"] = str(int(number))

                self.rhp = extraction["periodo_detenzione_raccomandato"]
            else:
                self.rhp = "multiple"

        except Exception as error:
            print("extract general data error" + repr(error))
            error_list = ["isin", "indicatore_sintetico_rishio"]
            extraction = {key: (extraction[key] if extraction.get(key) is not None else "ERROR") for key in error_list}
            self.rhp = extraction["periodo_detenzione_raccomandato"] = "multiple"

        return extraction

    def extract_isin(self):
        to_search = self.text[0].page_content[20:-3]#.replace('\n', ' ')
        isin = re.search(r"[A-Z]{2}[A-Z0-9]{9}\d", to_search)
        return isin.group(0) if isin else "-"
    
    def is_product_complex(self):
        """extracts if the product is complex

        Returns:
            dict(): extracted data
        """
        try:
            schema = self.extraction_config['tag'].get('is_complex')
            extraction = Models.tag(self.text[0].page_content[:1800], schema, self.file_id)
            extraction = {'is_product_complex':  'true' if extraction.is_disclaimer_there else 'false'}
            
            return extraction
        except Exception as error:
            print("is_product_complex error" + repr(error))
            return dict([("ERROR", "ERROR")])
    
    def extract_underlying_info(self, isin, table):
        """extracts underlying type

        Returns:
            dict(): extracted data
        """
        try:
            if isin != "-":
                extraction = {
                    "underlying_type": "fondo esterno",
                    "underlying_name": isin,
                }
            else:

                # Select first half of first page
                leng = len(self.text[0].page_content)
                text = self.text[0].page_content[:int(leng)]
                prompt = """Considera la prima pagina del documento di un prodotto. Estraendo le informazioni necessarie utilizzando
                le seguenti indicazioni.
                - non considerare le informazioni inerenti al prodotto ma allo specifico investimento. (il documento fa parte di possibili modalità di investimento
                di un prodotto, duqnue potrebbero esserci anche informazioni del prodotto in generale che però non vanno considerate)
                - non considerare cosa potrebbe fare l'investitore o  il prodotto in sè ma in cosa investe l'opzione di investimento
                ###
                DOCUMENTO: {}
                """.format(self.text[0].page_content)
                underlying_schema = self.extraction_config['tag'].get('underlying_info')
                #schema = table_schemas['it']['underlying_info']
                extraction = Models.tag(prompt, schema, self.file_id)
                # extraction = llm_extraction_and_tag(self.text, self.language, 'underlying_type', self.file_id)
                # extraction = clean_response_strips("underlying_type", self.language, extraction)
                return extraction
        except Exception as error:
            print("extract underlying type error" + repr(error))
            return dict([("ERROR", "ERROR")])
    
    def extract_market(self, market_type="target_market"):
        """extracts market from the document

        Args:
            market_type (str, optional): type of market to extract. Defaults to "market".
                Can also be "maket_gkid".

        Returns:
            dict(): market extracted
        """
        market = None
        try:
            template = self.extraction_config['prompt'].get(market_type)
            market = llm_extraction(self.text[0], template, self.file_id)
            # procedural cleaning
            market = clean_response_strips("market", self.language, market)

        except Exception as error:
            print("market extraction error" + repr(error))
            if not market:
                market = "ERROR"

        market = dict([("target_market", market)])
        return market

    # OLD METHOD
    # def extract_riy(self, page=1):
    #     """extracts riy from the document

    #     Returns:
    #         dict(): riy extracted
    #     """
    #     try:
    #         # Select page with RIY
    #         extraction_riy = tag_only(self.text[page:], "riy", self.language, self.file_id, rhp=self.rhp)
    #         extraction_riy = clean_response_regex("riy", self.language, extraction_riy)
    #     except Exception as error:
    #         print("extract riy error" + repr(error))
    #         error_list = ["incidenza_costo_1", "incidenza_costo_rhp"]

    #         extraction_riy = {
    #             key: (extraction_riy[key] if extraction_riy.get(key) is not None else "ERROR") for key in error_list
    #         }

    #     return extraction_riy
    
    def extract_riy(self):
        """extracts riy from the document

        Returns:
            dict(): riy extracted
        """
        try:
            riy_wr = self.extraction_config['word_representation'].get('riy')
            riy_schema = self.extraction_config['tag'].get('riy')
            rhp = int(self.rhp)
            
            # Set starting page & select desired page
            strat_page = 0 if len(self.text) < 3 else 1
            reference_text = self.text[strat_page:]
            page = select_desired_page(reference_text, riy_wr)
            page = reference_text[int(page)]
            
            # If RHP >=10 we also need to get the values at RHP/2
            if rhp >=10:
                year = ceil(rhp/2)
                riy_rhp2_prompt = self.extraction_config['prompt'].get('riy_rhp_2')
                riy_rhp2_schema = self.extraction_config['tag'].get('riy_rhp_2')
             
                total_prompt = riy_rhp2_prompt.format(year, rhp, page.page_content)
                extraction_riy = Models.tag(total_prompt, riy_rhp2_schema, self.file_id)         
            else:
                riy_prompt = self.extraction_config['prompt'].get('riy')
                
                total_prompt = riy_prompt.format(rhp, page.page_content)
                extraction_riy = Models.tag(total_prompt, riy_schema, self.file_id)
            extraction_riy = dict(extraction_riy)
            for key in extraction_riy:
                # Check if the value is a float
                if isinstance(extraction_riy[key], float):
                    extraction_riy[key] = str(extraction_riy[key]).replace('.', ',')
            # Clean response
            extraction_riy = clean_response_regex("riy", self.language, extraction_riy)

            
        except Exception as error:
            print("extract riy error" + repr(error))
            error_list = [k for k in riy_schema.schema()['properties'].keys()]
            extraction_riy = {
                key: "ERROR" for key in error_list
            }
    
        return extraction_riy
    
    def extract_riy_small(self):
        """extracts riy from the document

        Returns:
            dict(): riy extracted
        """
        try:
            # Find page with RIY
            riy_wr = self.extraction_config['word_representation'].get('riy')
            # Set starting page & select desired page
            strat_page = 0 if len(self.text) < 3 else 1
            reference_text = self.text[strat_page:]
            page = select_desired_page(reference_text, riy_wr)
            
            # Create prompt
            riy_small_schema = self.extraction_config['tag'].get('riy_small')
            riy_small_prompt = self.extraction_config['prompt'].get('riy_small')
            rhp = int(self.rhp)
            page = reference_text[int(page)]          
            total_prompt = riy_small_prompt.format(rhp, page.page_content)

            # Extraction and cleaning
            extraction_riy = Models.tag(total_prompt, riy_small_schema, self.file_id)         
            extraction_riy = clean_response_regex("riy", self.language, extraction_riy)
            
        except Exception as error:
            print("extract riy error" + repr(error))
            error_list = [k for k in riy_small_schema.schema()['properties'].keys()]
            performance = {
                key: (performance[key] if performance.get(key) is not None else "ERROR") for key in error_list
            }
    
        return extraction_riy
    
    #REVIEW: NEED TO UPLOAD TABLE AS DF
    def extract_entryexit_costs(self, table):

        try:
            entry_exity_schema = self.extraction_config['tag'].get('costi_ingresso')
            table =  upload_df_as_excel(table)
            extraction = general_table_inspection(
                table,
                entry_exity_schema,
                self.file_id,
                add_text="estrai il valore % dopo {} anni".format(self.rhp),
            )
            extraction = clean_response_regex("costi_ingresso", self.language, extraction)
        except Exception as error:
            print("extract entry exit costs error" + repr(error))
            error_list = ["costi_ingresso", "costi_uscita"]
            extraction = {key: (extraction[key] if extraction.get(key) is not None else "ERROR") for key in error_list}

        return extraction
    


    # REVIEW: NEED TO UPLOAD TABLE AS DF
    def extract_management_costs(self, table):

        try:
            extraction = dict()
            management_costs_schema = self.extraction_config['tag'].get('costi_gestione')
            table =  upload_df_as_excel(table)
            extraction = general_table_inspection(
                table,
                management_costs_schema,
                self.file_id,
                add_text="estrai il valore % dopo {} anni".format(self.rhp),
            )
            extraction = clean_response_regex("costi_gestione", self.language, extraction)
        except Exception as error:
            print("extract management costs error" + repr(error))
            error_list = ["commissione_gestione", "commissione_transazione", "commissione_performance"]
            extraction = {key: (extraction[key] if extraction.get(key) is not None else "ERROR") for key in error_list}

        return extraction
    

    def extract_performances(self, table):
        """extracts performances from scenarios in the document

        Args:
            table (pandas.dataframe): table containing the performances

        Returns:
            dict(): dict containing the performances
        """
        performance_res = dict()
        try:

            rhp = int(self.rhp)
            performance_prompt = self.extraction_config['prompt'].get('performance')
            performance_schema = self.extraction_config['tag'].get('performance')

            table = table[~table.iloc[:, 0].str.contains('caso vita', case=False, na=False)]
            table = table[~table.iloc[:, 0].str.contains('importo investito nel tempo', case=False, na=False)]
            table = table.reset_index(drop=True)
            # Fill row names where empty
            table = self.__adjust_performance_table(table, 'stress')
            table = self.__adjust_performance_table(table, 'sfavorevole')
            table = self.__adjust_performance_table(table, 'moderato')
            table = self.__adjust_performance_table(table, 'favorevole')
            table_upload = upload_df_as_excel(table)
                    
            adapt_extraction = performance_prompt.format(rhp=rhp, context=table_upload)
                    # Tagging
            performance_res = Models.tag(adapt_extraction, performance_schema, self.file_id)
            
            performance_res = dict(performance_res)
            morte = {
                "scenario_morte_1": performance_res.get("scenario_morte_1"),
                "scenario_morte_rhp": performance_res.get("scenario_morte_rhp")
                }
       
            performance_res = clean_response_regex("performance", self.language, performance_res)
            morte = clean_response_regex("performance_morte", self.language, morte)
            performance_res["scenario_morte_1"] = morte.get("scenario_morte_1")
            performance_res["scenario_morte_rhp"] = morte.get("scenario_morte_rhp")
        except Exception as error:
            print("extract performances error" + repr(error))
            error_list = [k for k in performance_schema.schema()['properties'].keys()]
            performance_res = {
                key: (performance_res[key] if performance_res.get(key) is not None else "ERROR") for key in error_list
            }

        return performance_res

    def extract_performances_abs(self, table, rhp):
        """extracts performances from scenarios in the document

        Args:
            table (pandas.dataframe): table containing the performances

        Returns:
            dict(): dict containing the performances
        """
        performance = dict()
        try:
            performance_abs_schema = self.extraction_config['tag'].get('performance_abs')
            performance_abs_prompt = self.extraction_config['prompt'].get('performance_abs')
            # eliminate the row where 'minimo' is mentioned
            # SOlo per il primo valore in cui minimo è presente
            table = table[~table.iloc[:, 0].str.contains('caso vita', case=False, na=False)]
            table = table[~table.iloc[:, 0].str.contains('importo investito nel tempo', case=False, na=False)]
            table = table.drop(table.iloc[:, 0].str.contains('minimo', case=False, na=False).idxmax())
            table = table[~table.iloc[:, 0].str.contains('scenario di morte', case=False, na=False)]
            table = table[~table.iloc[:, 0].str.contains('decesso dell\'assicurato', case=False, na=False)]

            table = table.reset_index(drop=True)
            # Fill row names where empty
            table = self.__adjust_performance_table(table, 'stress')
            table = self.__adjust_performance_table(table, 'sfavorevole')
            table = self.__adjust_performance_table(table, 'moderato')
            table = self.__adjust_performance_table(table, 'favorevole')

            table_upload = upload_df_as_excel(table)

            if rhp is None:
                adapt_extraction = "CONSIDERA 1 ANNO , EXTRACTION={}".format(table_upload)
            else:
                adapt_extraction = performance_abs_prompt.format(rhp=rhp, context=table_upload)

            # Extract performances                        
            performance_abs_res = Models.tag(adapt_extraction, performance_abs_schema, self.file_id)
            performance_abs_res = clean_response_regex("performance_abs", self.language, performance_abs_res)

        except Exception as error:
            print("extract performances error" + repr(error))
            error_list = [k for k in performance_abs_schema.schema()['properties'].keys()]
            performance_abs_res = {
                key: (performance[key] if performance.get(key) is not None else "ERROR") for key in error_list
            }

        return performance_abs_res

    def extract_performances_rhp_2(self, table, rhp):
            """extracts performances from scenarios in the document

            Args:
                table (pandas.dataframe): table containing the performances

            Returns:
                dict(): dict containing the performances
            """
            performance_rhp_2_res = dict()
            try:
                rhp= int(rhp)
                #schema = table_schemas['it']['performance_rhp_2']
                performance_rhp2_schema = self.extraction_config['tag'].get('performance_rhp_2')
                if rhp is not None and rhp >=10:
                    
                    year = ceil(rhp/2)
                    
                    # Adjust table
                    table = table[~table.iloc[:, 0].str.contains('caso vita', case=False, na=False)]
                    table = table[~table.iloc[:, 0].str.contains('importo investito nel tempo', case=False, na=False)]
                    # Drop the FIRST row where 'minimo' is mentioned
                    table = table.drop(table.iloc[:, 0].str.contains('minimo', case=False, na=False).idxmax())
                    # Drop last col (used for RHP's values)
                    table = table.iloc[:, :-1]

                    # Fill row names where empty
                    table = table.reset_index(drop=True)
                    table = self.__adjust_performance_table(table, 'stress')
                    table = self.__adjust_performance_table(table, 'sfavorevole')
                    table = self.__adjust_performance_table(table, 'moderato')
                    table = self.__adjust_performance_table(table, 'favorevole')

                    # Get table from excel & create prompt
                    table_upload = upload_df_as_excel(table)
                    performance_rhp2_prompt = self.extraction_config['prompt'].get('performance_rhp_2')
                    adapt_extraction = performance_rhp2_prompt.format(year=year, context=table_upload)
                    # Tagging
                    performance_rhp_2_res = Models.tag(adapt_extraction, performance_rhp2_schema, self.file_id)
                    performance_rhp_2_res = clean_response_regex("performance_rhp_2", self.language, performance_rhp_2_res)
                else:
                    performance_rhp_2_res = dict()
                    for k in performance_rhp2_schema.schema()['properties'].keys():
                        performance_rhp_2_res[k] = ""

            except Exception as error:
                print("extract performances error" + repr(error))
                error_list = [k for k in performance_rhp2_schema.schema()['properties'].keys()]
                performance_rhp_2_res = {
                    key: (performance_rhp_2_res[key] if performance_rhp_2_res.get(key) is not None else "ERROR") for key in error_list
                }

            return performance_rhp_2_res
    
    def __adjust_performance_table(self, table, word_to_adjust):
        """Adjusts the table by filling the row names where empty

        Args:
            table (pd.DataFrame): table to adjust
            word_to_adjust (str): word to adjust in the dataframe cell

        Returns:
            pd.DataFrame: Adjsuted dataframe
        """
        word_mask = table.iloc[:, 0].str.contains(word_to_adjust, case=False, na=False)
        stress_index = word_mask.index[word_mask].tolist()
        for i in stress_index:
            # If the row is empty, fill it with the word to adjust
            if table.iloc[i-1, 0] == '':
                table.iloc[i-1, 0] = word_to_adjust
    
        return table
    

if __name__ == "__main__":
    # testing
    doc_folder = "data\C\MEDIOLANUM\MYLIFEPIC_FR0011660851.pdf"
    kid_extractor = KidExtractor(doc_folder)
