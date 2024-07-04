
import os
from concurrent.futures import ProcessPoolExecutor
from AWSInteraction.EnvVarSetter import EnvVarSetter
# from extractors.general_extractors.custom_extractors.certificates.issuers.BNP_extractor import BNPDerivatiKidExtractor

# from extractors.general_extractors.custom_extractors.certificates.issuers.Vontobel_extractor import VontobelDerivatiKidExtractor

# from extractors.general_extractors.custom_extractors.certificates.issuers.Leonteq_extractor import LeonteqDerivatiKidExtractor


# # from extractors.Derivati.Spot_KID_extractor import write_info
# # from extractors.Derivati.Global_KID_extractor import GlobalExtractor
from extractors.models import Models
from extractors.general_extractors.config.prompt_config import table_schemas
from extractors.general_extractors import utils

# import glob
# import logging
# import asyncio
# import pandas as pd
# from functools import partial

# logging.basicConfig(filename="logging.log", encoding="utf-8", level=logging.DEBUG)


# def process_file(file_path, file_type):
#     """instanciate a KidExtractor and process the file

#     Args:
#         file_path (str): path of pdf file to process

#     Returns:
#         dict(filename,dict()): dictionary containing the results for the file
#     """
#     try:
#         match file_type:
#             # case "kid":
#             #     extractor = InsuranceKidExtractor(file_path)
#             # case "gkid":
#             #     extractor = InsuranceGKidExtractor(file_path)
#             case "leonteq":
#                 extractor = LeonteqDerivatiKidExtractor(file_path)
#             case "bnp":
#                 extractor = BNPDerivatiKidExtractor(file_path)
#             case "vontobel":
#                 extractor = VontobelDerivatiKidExtractor(file_path)
#             case _:
#                 raise ValueError("type not supported")
            
#         return asyncio.run(extractor.process())
    
    
#     except Exception as error:
#         print("ERROR: {}".format(file_path) + repr(error))
#         filename = os.path.splitext(os.path.basename(file_path))[0]
#         return dict((filename, dict()))


# def main(doc_folder):
#     """main loop, instanciate 10 async process(more causes errors) for 10 files at the time,
#     puts results in an excel file

#     Args:
#         doc_folder (str): folder containing the pdf files
#     """
#     try:
#         env_setter = EnvVarSetter()
#         env_setter.configure_local_env_vars()
#         # testing
#         file_type = "bnp"
#         all_files = []
#         # list all the pdf files in the folder
#         print("START")
#         all_files = glob.glob(os.path.join(doc_folder, "**\\*.pdf"), recursive=True)
#         results = {}

#         # partial_process_file = partial(process_file, file_type=file_type)
#         # # async processing of the files
#         # with ProcessPoolExecutor(max_workers=1) as executor:
#         #     results = executor.map(partial_process_file, all_files)
#         for file in all_files:
#             results = process_file(file, file_type)
#         # give request id
#         Models.clear_resources_group(str(-1))
#         # orders results
#         results = pd.DataFrame(results)
#         #ordered = [col for col in column_order[file_type] if col in results.columns]
#         #results = results[ordered]
#         excel_path = os.path.join(doc_folder + '.xlsx')
#         # saves results
#         results.to_excel(excel_path, header=True, index=False)
#         print(results)

#     except Exception as error:
#         print("top level error:" + repr(error))


# if __name__ == "__main__":

#     folder = "dati\\derivati\\bnp"
    
#     #for root, dirs, files in os.walk(folder):
#         # Check if there are PDF files in the current directory
#         #if any(file.endswith(".pdf") for file in files):
#             # Call your existing function to process PDFs in the folder
#     main(folder)

#     # main(folder)

# Initialize and set environment variables
env_setter = EnvVarSetter()
env_setter.configure_local_env_vars()

company_schema = "company_name"  # Schema category
file_id = "unique_identifier_for_file_process"  # Example file identifier, we are not using this in the code, so just pass any string
def extract_company_name(text, company_schema, file_id):
    """Extracts company name from the given text using a predefined schema and tagging mechanism."""
    pydantic_class = table_schemas["it"][company_schema]  # "it" is assumed to be the language or schema category
    raw_extraction = Models.tag(text, pydantic_class, file_id)
    return raw_extraction




t_path = r"C:\Users\ribhu.kaul\RibhuLLM\PageFinder\1ARCA\arca\arca_18.pdf"
t =utils.get_document_text(t_path)
t1 = [t[0], t[1]]

t1_object = extract_company_name(t1, company_schema=company_schema, file_id=file_id)
t1_name = t1_object.company_name if hasattr(t1_object, 'company_name') else 'DefaultCompanyName'
print(t1_name)