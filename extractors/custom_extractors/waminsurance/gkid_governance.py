import os

from extractors.models import Models
from extractors.general_extractors.custom_extractors.kid.gkid_extractor import GKidExtractor


class WamInsuranceGKidGovernanceExtractor(GKidExtractor):

    def __init__(self, doc_path) -> None:
        self.doc_path = doc_path
        self.tenant = "waminsurance"
        self.extractor = "gkidgovernance"
        super().__init__(doc_path, "it", tenant=self.tenant, extractor=self.extractor)

    def process(self):
        """main processor in different phases.

        Returns:
            dict(filename,dict()): dictionary containing the results for the file
        """
        # first phase for essenctial data for second phase and general information
        try:
            functions_parameters = {
                "tables": {"function": self.get_tables},
                "basic_information": {"function": self.extract_general_data},
                "market": {"function": self.extract_market},
                "is_product_complex": {"function": self.is_product_complex},
            }
            results = self.threader(functions_parameters)
            tables = results["tables"]
            basic_information = results["basic_information"]
            market = results["market"]
            is_product_complex = results["is_product_complex"]
           

        except Exception as error:
            print("first stage error" + repr(error))
        # second phase for all the rest
        try:
            functions_parameters = {
                "riy": {"function": self.extract_riy, "args": {"table": tables["riy"]}},
                "costs": {"function": self.extract_cost_commissions, "args": {"table_ingresso": tables["costi_ingresso"], "table_gestione": tables["costi_gestione"]}},
            }
            results = self.threader(functions_parameters)
            riy, costs = results["riy"], results["costs"]

        except Exception as error:
            print("second stage error" + repr(error))

        try:
            # REVIEW: what name do they need?
            filename = os.path.splitext(os.path.basename(self.doc_path))[0]
            api_costs = self._process_costs()
            complete_dict = {
                "file_name": filename,
                **dict(basic_information),
                **dict(riy),
                **dict(costs),
                **dict(market),
                **dict(is_product_complex),
                "api_costs": api_costs,
            }

            # raccordo
            fromatted_output = self.create_output(complete_dict)
              
        except Exception as error:
            print("dictionary error" + repr(error))
            filename = os.path.splitext(os.path.basename(self.doc_path))[0]
            fromatted_output = dict([(filename), dict()])
        print(fromatted_output)
        Models.clear_resources_file(filename)

        return fromatted_output

