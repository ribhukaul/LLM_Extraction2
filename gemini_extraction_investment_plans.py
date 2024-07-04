# from models.gemini.gemini_multimodal import get_file, create_model
# from extractors.models import Models
# from extractors.general_extractors.config.prompt_config import table_schemas
# from AWSInteraction.EnvVarSetter import EnvVarSetter
# import json
# import pandas as pd
# from typing import List
# from pydantic import BaseModel, Field
# from typing import Optional
# import os
# import re




# # Load the example prompts  
# from prompts.certificates.test_prompt_complexity.example_prompt_1 import prompt_example_1, prompt_example_3, prompt_example_4, prompt_example_6

# # Create the generative model
# project="pftpro-167412"
# location="us-central1"
# model_version = "gemini-1.5-flash"
# # "gemini-1.5-flash"
# # "gemini-1.5-pro-preview-0409"
# model = create_model(project, location, model_version)

# # Configuration for the generation
# generation_config = {
#     "max_output_tokens": 800,
#     "top_p": 0.95,
#     "temperature": 0,
# }


# path3 = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\Documenti\Condizioni_di_Assicurazione_InvestiPlan.pdf"



# mid_processing = get_file(path3)
# prompt_example_4.append(mid_processing)




# test_response3 = model.generate_content(prompt_example_4, generation_config=generation_config)
# print(test_response3)


# def extract_text_from_response(response):
#     """ Safely extracts text from a nested response object. """
#     try:
#         # Accessing text assuming 'response' is a class with attribute access
#         return response.candidates[0].content.parts[0].text
#     except (AttributeError, IndexError) as e:
#         # If the structure is different or parts are missing, return an empty string
#         print(f"Error accessing text: {e}")
#         return ""

# # Let's assume test_response3 is already fetched and is a correct object
# response_text = extract_text_from_response(test_response3)

# # Extract fund names from the text
# fund_names = re.findall(r'-\s*([^:\n]+)', response_text)

# # Load the PDF file name

# filename = os.path.basename(path3)

# # Remove file extension and replace it with '.xlsx'
# excel_filename = filename.replace('.pdf', '.xlsx')

# # Specify the full path for the output Excel file
# excel_output_path = os.path.join(r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\processing", excel_filename)

# # Create a DataFrame to hold the fund names and the associated file name
# df = pd.DataFrame(fund_names, columns=['Fund Name'])
# df['File Name'] = filename

# # Save the DataFrame to an Excel file
# df.to_excel(excel_output_path, index=False)

# print(f"Excel file successfully saved to {excel_output_path}")


################################################################


######################################################## WORKS FINE

# import os
# import pandas as pd
# import re
# from concurrent.futures import ProcessPoolExecutor
# from prompts.certificates.test_prompt_complexity.example_prompt_1 import prompt_example_1, prompt_example_3, prompt_example_4, prompt_example_6
# from models.gemini.gemini_multimodal import get_file, create_model

# # Output File for LLM Responses
# output_file_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\llm_response_nodata.txt"
#     # "C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\llm_response_nodata.txt"
#     # "C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\llm_response_missed_flash.txt"
#     # "C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\llm_response_actual_flash.txt"
# combined_excel_output_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\combined_results_missed_unopened.xlsx"
# open(output_file_path, "w").close()  # Clear existing content

# def process_file(file_path):
#     project = "pftpro-167412"
#     location = "us-central1"
#     model_version = "gemini-1.5-flash"   # "gemini-1.5-pro-preview-0409"     "gemini-1.5-flash"
#     model = create_model(project, location, model_version)
#     generation_config = {"max_output_tokens": 8000, "top_p": 0.95, "temperature": 0}

#     try:
#         mid_processing = get_file(file_path)
#         prompt_example_4.append(mid_processing)

#         test_response3 = model.generate_content(prompt_example_4, generation_config=generation_config)
#         print(test_response3)

#         response_text = test_response3.candidates[0].content.parts[0].text
#         # Adjust the regular expression to match the actual format of the fund names
#         fund_names = re.findall(r"'(.*?)':", response_text)
#     except (AttributeError, IndexError) as e:
#         print(f"Error accessing text in {file_path}: {e}")
#         return file_path, None  # Return the file path and None if an error occurs
#     except Exception as e:
#         print(f"Error processing file '{file_path}': {e}")
#         return file_path, None  # Return the file path and None if any other error occurs

#     # Save to Excel
#     filename = os.path.basename(file_path)
#     excel_filename = filename.replace('.pdf', '.xlsx')
#     excel_output_path = os.path.join(
#         os.path.dirname(file_path).replace("opened_but_noDataRead", "processing_nodata"), excel_filename # "processing_actual_flash" "processing_missed_flash"   "processing_nodata"
#     )
#     df = pd.DataFrame(fund_names, columns=['Fund Name'])
#     df['File Name'] = filename
#     df.to_excel(excel_output_path, index=False)
    
#     # Save LLM Output with File Name
#     with open(output_file_path, "a") as f:
#         f.write(f"############# {filename} #############\n")
#         f.write(response_text + "\n\n")

#     return None, df  # Return None and the DataFrame if processing was successful

# def main():
#     directory = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\Unprocessed\opened_but_noDataRead"
#      #"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\Documenti1"
#     # "C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\Unprocessed
#     # "C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\Unprocessed\opened_but_noDataRead"
#     files_to_process = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.pdf')]
    
#     unprocessed_files = []
#     all_dataframes = []
    
#     with ProcessPoolExecutor() as executor:
#         results = executor.map(process_file, files_to_process)
    
#     for file_path, result in zip(files_to_process, results):
#         if result[0] is not None:
#             unprocessed_files.append(result[0])
#         if result[1] is not None:
#             all_dataframes.append(result[1])
    
#     if unprocessed_files:
#         print("The following files were not processed successfully:")
#         for file in unprocessed_files:
#             print(file)
#     else:
#         print("All files processed successfully.")

#     # Combine all dataframes into one and save to a single Excel file
#     if all_dataframes:
#         combined_df = pd.concat(all_dataframes, ignore_index=True)
#         combined_df.to_excel(combined_excel_output_path, index=False)
#         print(f"Combined results saved to {combined_excel_output_path}")

# if __name__ == "__main__":
#     main()
############################################################## This one also works fine, don't delete yet
# import os
# import pandas as pd
# import re
# from concurrent.futures import ProcessPoolExecutor
# from prompts.certificates.test_prompt_complexity.example_prompt_1 import prompt_example_1, prompt_example_3, prompt_example_4, prompt_example_6
# from models.gemini.gemini_multimodal import get_file, create_model

# # Output File for LLM Responses
# output_file_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\llm_response_nodata.txt"
# combined_excel_output_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\combined_results_missed_unopened.xlsx"
# open(output_file_path, "w").close()  # Clear existing content

# def process_file(file_path, file_index):
#     project = "pftpro-167412"
#     location = "us-central1"
#     model_version = "gemini-1.5-flash"
#     model = create_model(project, location, model_version)
#     generation_config = {"max_output_tokens": 8000, "top_p": 0.95, "temperature": 0}

#     try:
#         mid_processing = get_file(file_path)
#         prompt_example_4.append(mid_processing)

#         test_response3 = model.generate_content(prompt_example_4, generation_config=generation_config)
#         print(test_response3)

#         response_text = test_response3.candidates[0].content.parts[0].text
#         # Adjust the regular expression to match the actual format of the fund names
#         fund_names = re.findall(r"\'(.*?)\' : \'fondo (?:interno|esterno)\'", response_text)
        
#         # Debug: Print extracted fund names
#         print(f"Extracted fund names from {file_path}: {fund_names}")
        
#         if not fund_names:
#             print(f"No fund names extracted from {file_path}")
#             return file_path, None  # Return the file path and None if no fund names found
#     except (AttributeError, IndexError) as e:
#         print(f"Error accessing text in {file_path}: {e}")
#         return file_path, None  # Return the file path and None if an error occurs
#     except Exception as e:
#         print(f"Error processing file '{file_path}': {e}")
#         return file_path, None  # Return the file path and None if any other error occurs

#     # Save to Excel
#     filename = os.path.basename(file_path)
#     excel_filename = filename.replace('.pdf', '.xlsx')
#     excel_output_path = os.path.join(
#         os.path.dirname(file_path).replace("opened_but_noDataRead", "processing_nodata"), excel_filename
#     )

#     # Debug: Print Excel output path
#     print(f"Saving DataFrame to {excel_output_path}")
    
#     df = pd.DataFrame(fund_names, columns=['Fund Name'])
#     df['File Name'] = filename
#     df.to_excel(excel_output_path, index=False)
    
#     # Debug: Confirm DataFrame content
#     print(f"DataFrame content to be saved:\n{df}")
    
#     # Save LLM Output with File Name
#     with open(output_file_path, "a") as f:
#         f.write(f"############# {file_index} {filename} #############\n")
#         f.write(response_text + "\n\n")

#     return None, df  # Return None and the DataFrame if processing was successful

# def main():
#     directory = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\Unprocessed\opened_but_noDataRead"
#     files_to_process = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.pdf')]
    
#     unprocessed_files = []
#     all_dataframes = []
    
#     with ProcessPoolExecutor(max_workers=3) as executor:  # Limit to 3 parallel processes
#         results = executor.map(process_file, files_to_process, range(1, len(files_to_process) + 1))
    
#     for file_path, result in zip(files_to_process, results):
#         if result[0] is not None:
#             unprocessed_files.append(result[0])
#         if result[1] is not None:
#             all_dataframes.append(result[1])
    
#     if unprocessed_files:
#         print("The following files were not processed successfully:")
#         for file in unprocessed_files:
#             print(file)
#     else:
#         print("All files processed successfully.")

#     # Combine all dataframes into one and save to a single Excel file
#     if all_dataframes:
#         combined_df = pd.concat(all_dataframes, ignore_index=True)
#         combined_df.to_excel(combined_excel_output_path, index=False)
#         print(f"Combined results saved to {combined_excel_output_path}")

# if __name__ == "__main__":
#     main()


####################################################################
# This script processes PDF files for fund names extraction using a Gemini multimodal model.
# Key features:
# 1. Splits large PDF files exceeding the page limit (MAX_PAGES) into smaller parts.
# 2. Processes each PDF (or part of a split PDF) to extract fund names using the Gemini model.
# 3. Combines the extracted data from all processed files (including split parts) into a single Excel file.
# 4. Logs the number of LLM responses saved to a text file, appending the total count at the end.
# 5. Handles errors during processing and keeps track of unprocessed files for further inspection.
#
# This script ensures that large documents are handled appropriately by splitting them,
# while still maintaining a coherent structure of the extracted data.

# import os
# import pandas as pd
# import re
# from concurrent.futures import ThreadPoolExecutor  # Use ThreadPoolExecutor
# from PyPDF2 import PdfReader, PdfWriter
# from prompts.certificates.test_prompt_complexity.example_prompt_1 import prompt_example_1, prompt_example_3, prompt_example_4, prompt_example_6
# from models.gemini.gemini_multimodal import get_file, create_model
# import time

# # Output File for LLM Responses
# output_file_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\llm_responses_missed_flash2.txt"
# combined_excel_output_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\combined_results_test_missed2.xlsx"
# open(output_file_path, "w").close()  # Clear existing content

# MAX_PAGES = 300  # Maximum pages supported by the model
# RETRY_LIMIT = 3  # Number of times to retry on failure
# RETRY_DELAY = 5  # Delay in seconds between retries

# def split_pdf(file_path, max_pages=MAX_PAGES):
#     """ Split a PDF into smaller chunks if it exceeds the max_pages limit """
#     pdf_reader = PdfReader(file_path)
#     num_pages = len(pdf_reader.pages)
#     if num_pages <= max_pages:
#         return [file_path]

#     base_name = os.path.splitext(file_path)[0]
#     output_files = []
    
#     for i in range(0, num_pages, max_pages):
#         pdf_writer = PdfWriter()
#         for j in range(i, min(i + max_pages, num_pages)):
#             pdf_writer.add_page(pdf_reader.pages[j])
        
#         output_filename = f"{base_name}_part{i // max_pages + 1}.pdf"
#         with open(output_filename, 'wb') as output_pdf:
#             pdf_writer.write(output_pdf)
        
#         output_files.append(output_filename)
    
#     return output_files

# def process_file(file_path, file_index):
#     project = "pftpro-167412"
#     location = "us-central1"
#     model_version = "gemini-1.5-flash"
#     model = create_model(project, location, model_version)
#     generation_config = {"max_output_tokens": 8000, "top_p": 0.95, "temperature": 0}

#     for attempt in range(RETRY_LIMIT):
#         try:
#             mid_processing = get_file(file_path)
#             prompt_example_4.append(mid_processing)

#             test_response3 = model.generate_content(prompt_example_4, generation_config=generation_config)
#             print(test_response3)

#             response_text = test_response3.candidates[0].content.parts[0].text
#             # Adjust the regular expression to match the actual format of the fund names
#             fund_names = re.findall(r"\'(.*?)\' : \'fondo (?:interno|esterno)\'", response_text)
            
#             # Debug: Print extracted fund names
#             print(f"Extracted fund names from {file_path}: {fund_names}")
            
#             if not fund_names:
#                 print(f"No fund names extracted from {file_path}")
#                 return file_path, None  # Return the file path and None if no fund names found
            
#             # Save to Excel
#             filename = os.path.basename(file_path)
#             excel_filename = filename.replace('.pdf', '.xlsx')
#             excel_output_path = os.path.join(
#                 os.path.dirname(file_path).replace("Unprocessed", "processing_missed_flash"), excel_filename
#             )

#             # Debug: Print Excel output path
#             print(f"Saving DataFrame to {excel_output_path}")
            
#             df = pd.DataFrame(fund_names, columns=['Fund Name'])
#             df['File Name'] = filename
#             df.to_excel(excel_output_path, index=False)
            
#             # Debug: Confirm DataFrame content
#             print(f"DataFrame content to be saved:\n{df}")
            
#             # Save LLM Output with File Name
#             with open(output_file_path, "a") as f:
#                 f.write(f"############# {file_index} {filename} #############\n")
#                 f.write(response_text + "\n\n")

#             return None, df  # Return None and the DataFrame if processing was successful

#         except (AttributeError, IndexError) as e:
#             print(f"Error accessing text in {file_path}: {e}")
#             return file_path, None  # Return the file path and None if an error occurs
#         except Exception as e:
#             if "503" in str(e):
#                 print(f"Error processing file '{file_path}': {e}. Retrying in {RETRY_DELAY} seconds... (Attempt {attempt + 1} of {RETRY_LIMIT})")
#                 time.sleep(RETRY_DELAY)
#             else:
#                 print(f"Error processing file '{file_path}': {e}")
#                 return file_path, None  # Return the file path and None if any other error occurs

#     # If retries exhausted
#     print(f"Failed to process file '{file_path}' after {RETRY_LIMIT} attempts.")
#     return file_path, None

# def main():
#     directory = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\Unprocessed"
#     files_to_process = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.pdf')]
    
#     unprocessed_files = []
#     all_dataframes = []
#     response_count = 0
    
#     with ThreadPoolExecutor(max_workers=1) as executor:  # Limit to 1 parallel threads
#         split_files = [split_pdf(file) for file in files_to_process]
#         split_files_flat = [item for sublist in split_files for item in sublist]  # Flatten the list of lists
#         results = executor.map(process_file, split_files_flat, range(1, len(split_files_flat) + 1))
    
#     for file_path, result in zip(split_files_flat, results):
#         if result[0] is not None:
#             unprocessed_files.append(result[0])
#         if result[1] is not None:
#             all_dataframes.append(result[1])
#             response_count += 1
    
#     if unprocessed_files:
#         print("The following files were not processed successfully:")
#         for file in unprocessed_files:
#             print(file)
#     else:
#         print("All files processed successfully.")

#     # Combine all dataframes into one and save to a single Excel file
#     if all_dataframes:
#         combined_df = pd.concat(all_dataframes, ignore_index=True)
#         combined_df.to_excel(combined_excel_output_path, index=False)
#         print(f"Combined results saved to {combined_excel_output_path}")
    
#     # Append the response count to the output file
#     with open(output_file_path, "a") as f:
#         f.write(f"\nTotal LLM Responses Saved: {response_count}\n")

# if __name__ == "__main__":
#     main()


###################################################

"""
This script processes a collection of PDF files to extract fund names using the Gemini model.
It includes the following functionalities:

1. Splitting Large PDFs: 
   - PDFs exceeding a specified number of pages (MAX_PAGES) are split into smaller chunks to comply with the model's page limit.
   - This helps in handling documents that would otherwise exceed the model's capabilities.

2. Serial Processing of PDF Files: 
   - The script processes files sequentially (one at a time) to avoid issues related to concurrent processing.
   - This is achieved by iterating over each file and processing it without using parallel processing techniques.

3. Retrying on Failure: 
   - If a file fails to process due to certain errors (e.g., network issues or temporary unavailability), 
     the script retries processing up to a specified number of times (RETRY_LIMIT) with a delay between attempts (RETRY_DELAY).

4. Saving Outputs: 
   - The extracted fund names are saved to individual Excel files for each processed PDF.
   - All extracted data is also combined into a single Excel file.
   - The script logs the LLM responses to a text file and counts the number of successful extractions, appending this count to the text file.

This version of the script is intended to ensure robustness in handling large documents and to provide clarity in the output by saving each 
successful response and maintaining a count of total responses.

Usage:
- Update the directory paths and parameters (e.g., MAX_PAGES, RETRY_LIMIT) as needed.
- Run the script to process the PDF files in the specified directory.
"""
              
###################################################
# import os
# import pandas as pd
# import re
# import json
# from PyPDF2 import PdfReader, PdfWriter
# from prompts.certificates.test_prompt_complexity.example_prompt_1 import prompt_example_1, prompt_example_3, prompt_example_4, prompt_example_6
# from models.gemini.gemini_multimodal import get_file, create_model
# import time

# # Output File for LLM Responses
# output_file_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\llm_responses_test_flash_serialDB.txt"
# combined_excel_output_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\combined_results_test_serialDB.xlsx"
# open(output_file_path, "w").close()  # Clear existing content

# MAX_PAGES = 300  # Maximum pages supported by the model
# RETRY_LIMIT = 3  # Number of times to retry on failure
# RETRY_DELAY = 5  # Delay in seconds between retries
# MAX_TOKENS = 8000  # Maximum tokens supported by the model

# text_6c_2 = """ Di seguito è riportato un documento relativo ad un prodotto assicurativo con l'elenco di tutti gli asset sottostanti in cui è possibile investire il prodotto.
# Estrarre in modo strutturato tutti i fondi interni, i fondi esterni e le gestioni separate in cui il prodotto può investire fornendo in output un dizionario, con come chiave il nome del fondo e la tipologia di fondo (fondo interno, fondo esterno o separato gestione) come valore . I nomi dei fondi POSSONO ESSERE TROVATI NELLA colonna con l'intestazione "denominazione fondo" o "Denominazione". Di seguito è riportato anche un esempio di output:
# -----
# ESEMPIO
# {
# 'BOTTOM 1 NAME': 'fondo interno',
# 'BOTTOM 2 NAME': 'fondo esterno',
# 'NOME FONDO 3': 'gestione separata',
# eccetera.
# }
# ------
# DOCUMENTO

# """

# def split_pdf(file_path, parts=2):
#     """ Split a PDF into a specified number of equal parts """
#     pdf_reader = PdfReader(file_path)
#     num_pages = len(pdf_reader.pages)
#     pages_per_part = max(1, num_pages // parts)
#     output_files = []
    
#     base_name = os.path.splitext(file_path)[0]

#     for part in range(parts):
#         start_page = part * pages_per_part
#         end_page = min(start_page + pages_per_part, num_pages)
#         if start_page >= num_pages:
#             break
#         pdf_writer = PdfWriter()
#         for page_num in range(start_page, end_page):
#             pdf_writer.add_page(pdf_reader.pages[page_num])
        
#         output_filename = f"{base_name}_part{part + 1}.pdf"
#         with open(output_filename, 'wb') as output_pdf:
#             pdf_writer.write(output_pdf)
        
#         output_files.append(output_filename)
#         print(f"Split {file_path} into {output_filename} (Pages {start_page}-{end_page - 1})")

#     return output_files

# # Define the clean_and_format_json function
# def clean_and_format_json(json_str):
#     # Ensure the input is a string
#     if not isinstance(json_str, str):
#         raise ValueError("Input must be a string")
    
#     # Step 1: Remove all quotes initially
#     cleaned_json_str = re.sub(r'["\']', '', json_str)
    
#     # Step 2: Add double quotes around keys (everything between { and :)
#     cleaned_json_str = re.sub(r'({\s*|\s*,\s*)([^:{}]+?)(\s*:)', r'\1"\2"\3', cleaned_json_str)
    
#     # Step 3: Add double quotes around values (everything between : and , or })
#     cleaned_json_str = re.sub(r'(:\s*)([^,{}]+?)(\s*(,|}))', r'\1"\2"\3', cleaned_json_str)
    
#     return cleaned_json_str

# # Define the clean_response_text function
# def clean_response_text(response_text):
#     # Replace non-standard quotation marks with standard ones
#     cleaned_response_text = response_text.replace('“', '"').replace('”', '"').replace("\\'", "'").replace('\\"', '"')
    
#     # Remove the backticks and `python` identifier
#     cleaned_response_text = cleaned_response_text.strip('```python').strip('```')

#     # Normalize whitespace and remove newlines
#     cleaned_response_text = cleaned_response_text.replace('\n', ' ').replace('\r', '')
#     cleaned_response_text = re.sub(r'\s+', ' ', cleaned_response_text).strip()

#     # Remove unnecessary escape characters
#     cleaned_response_text = re.sub(r'\\([nrt])', r'\1', cleaned_response_text)
#     cleaned_response_text = re.sub(r'\\{2,}', '', cleaned_response_text)
    
#     # Extract JSON-like content from response_text
#     json_content = re.search(r"\{.*?\}", cleaned_response_text, re.DOTALL)
#     if json_content:
#         json_str = json_content.group(0)
        
#         # Clean and format the JSON string
#         json_str = clean_and_format_json(json_str)
        
#         return json_str

#     return cleaned_response_text

# # Define the process_json_string function
# def process_json_string(json_str):
#     try:
#         json_data = json.loads(json_str)
#         return json_data, None
#     except json.JSONDecodeError as e:
#         error_index = e.pos
#         error_section = json_str[max(0, error_index-40):min(len(json_str), error_index+40)]
#         return None, error_section

# # Define the save_log function
# def save_log(file_path, log_message):
#     with open(file_path, 'a') as log_file:
#         log_file.write(log_message + "\n")

# # Define the process_file function
# def process_file(file_path, file_index):
#     project = "pftpro-167412"
#     location = "us-central1"
#     model_version = "gemini-1.5-flash"
#     model = create_model(project, location, model_version)
#     generation_config = {"max_output_tokens": MAX_TOKENS, "top_p": 0.95, "temperature": 0}

#     for attempt in range(RETRY_LIMIT):
#         try:
#             # Preserve the initial prompt text
#             prompt_example_4[:] = [text_6c_2]  # Preserve the initial text_6c_2

#             mid_processing = get_file(file_path)  # Breakpoint here to inspect mid_processing

#             if mid_processing:  # Ensure content is not empty
#                 prompt_example_4.append(mid_processing)  # Breakpoint here to verify prompt_example_4 contents
#             else:
#                 print(f"Invalid content in mid_processing for file: {file_path}, type: {type(mid_processing)}")
#                 return file_path, None

#             test_response3 = model.generate_content(prompt_example_4, generation_config=generation_config)  # Breakpoint here to inspect test_response3

#             response_text = test_response3.candidates[0].content.parts[0].text
#             usage_metadata = test_response3.usage_metadata  # Corrected to access usage_metadata properly
#             if usage_metadata.candidates_token_count >= MAX_TOKENS:  # Check token count if usage_metadata is available
#                 # Split the file again and process the new parts
#                 further_split_files = split_pdf(file_path, parts=2)
#                 return process_file(further_split_files[0], file_index)  # Process only the first part again

#             # Clean the response text using the defined function
#             cleaned_response_text = clean_response_text(response_text)

#             # Remove any code block formatting
#             cleaned_response_text = re.sub(r'```.*?```', '', cleaned_response_text, flags=re.DOTALL)

#             # Replace single quotes with double quotes for valid JSON
#             valid_json_str = cleaned_response_text.replace("'", '"')

#             # Extract JSON-like content from response_text
#             json_content = re.search(r"\{.*?\}", valid_json_str, re.DOTALL)
#             if json_content:
#                 json_str = json_content.group(0)
#                 print(f"Extracted JSON string: {json_str}") 
                
#                 # Call the process_json_string function
#                 funds_dict, error_section = process_json_string(json_str)
#                 if funds_dict:
#                     fund_names = list(funds_dict.keys())
#                     print(f"Parsed fund names: {fund_names}")  
#                 else:
#                     # Highlight the specific section causing the error
#                     print(f"JSON decoding error near: {error_section}")
#                     fund_names = []
#             else:
#                 fund_names = []

#             print(f"Extracted fund names from {file_path}: {fund_names}")
            
#             if response_text and not fund_names:
#                 pass

#             if not fund_names:
#                 return file_path, None  # Return the file path and None if no fund names found
            
#             # Save to Excel
#             filename = os.path.basename(file_path)
#             excel_filename = filename.replace('.pdf', '.xlsx')
#             excel_output_path = os.path.join(
#                 os.path.dirname(file_path).replace("micro_testing", "processing_test_flash_serial"), excel_filename
#             )

#             df = pd.DataFrame(fund_names, columns=['Fund Name'])
#             df['File Name'] = filename
#             df.to_excel(excel_output_path, index=False)
            
#             # Save LLM Output with File Name in the correct path
#             with open(output_file_path, "a") as f:
#                 f.write(f"############# {file_index} {filename} #############\n")
#                 f.write(response_text + "\n\n")

#             return None, df  # Return None and the DataFrame if processing was successful

#         except (AttributeError, IndexError) as e:
#             print(f"Error accessing text in {file_path}: {e}")
#             return file_path, None  # Return the file path and None if an error occurs
#         except Exception as e:
#             if "503" in str(e):
#                 print(f"Error processing file '{file_path}': {e}. Retrying in {RETRY_DELAY} seconds... (Attempt {attempt + 1} of {RETRY_LIMIT})")
#                 time.sleep(RETRY_DELAY)
#             else:
#                 print(f"Error processing file '{file_path}': {e}")
#                 return file_path, None  # Return the file path and None if any other error occurs

#     # If retries exhausted
#     print(f"Failed to process file '{file_path}' after {RETRY_LIMIT} attempts.")
#     return file_path, None


# def main():
#     directory = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\micro_testing"
#     files_to_process = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.pdf')]
    
#     unprocessed_files = []
#     all_dataframes = []
#     response_count = 0
    
#     for file_index, file_path in enumerate(files_to_process, start=1):
#         pdf_reader = PdfReader(file_path)
#         num_pages = len(pdf_reader.pages)
        
#         if num_pages > MAX_PAGES:
#             split_files = split_pdf(file_path, parts=2)  # Breakpoint here to check if the file is split
#         else:
#             split_files = [file_path]
        
#         for split_file_path in split_files:
#             result = process_file(split_file_path, file_index)  # Breakpoint here to debug process_file function
#             if result[0] is not None:
#                 unprocessed_files.append(result[0])
#             if result[1] is not None:
#                 all_dataframes.append(result[1])
#                 response_count += 1
    
#     if unprocessed_files:
#         print("The following files were not processed successfully:")
#         for file in unprocessed_files:
#             print(file)
#     else:
#         print("All files processed successfully.")

#     # Combine all dataframes into one and save to a single Excel file
#     if all_dataframes:
#         combined_df = pd.concat(all_dataframes, ignore_index=True)
#         combined_df.to_excel(combined_excel_output_path, index=False)
#         print(f"Combined results saved to {combined_excel_output_path}")
    
#     # Append the response count to the output file
#     with open(output_file_path, "a") as f:
#         f.write(f"\nTotal LLM Responses Saved: {response_count}\n")

# if __name__ == "__main__":
#     main()

#######################################
import os
import pandas as pd
import re
import json
from PyPDF2 import PdfReader, PdfWriter
from prompts.certificates.test_prompt_complexity.example_prompt_1 import prompt_example_1, prompt_example_3, prompt_example_4, prompt_example_6
from models.gemini.gemini_multimodal import get_file, create_model
import time

# Output File for LLM Responses
output_file_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\llm_responses_test_flash_serialDB.txt"
combined_excel_output_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\combined_results_test_serialDB.xlsx"
open(output_file_path, "w").close()  # Clear existing content

MAX_PAGES = 300  # Maximum pages supported by the model
RETRY_LIMIT = 3  # Number of times to retry on failure
RETRY_DELAY = 5  # Delay in seconds between retries
MAX_TOKENS = 8000  # Maximum tokens supported by the model

text_6c_2 = """ Di seguito è riportato un documento relativo ad un prodotto assicurativo con l'elenco di tutti gli asset sottostanti in cui è possibile investire il prodotto.
Estrarre in modo strutturato tutti i fondi interni, i fondi esterni e le gestioni separate in cui il prodotto può investire fornendo in output un dizionario, con come chiave il nome del fondo e la tipologia di fondo (fondo interno, fondo esterno o separato gestione) come valore . I nomi dei fondi POSSONO ESSERE TROVATI NELLA colonna con l'intestazione "denominazione fondo" o "Denominazione". Di seguito è riportato anche un esempio di output:
-----
ESEMPIO
{
'BOTTOM 1 NAME': 'fondo interno',
'BOTTOM 2 NAME': 'fondo esterno',
'NOME FONDO 3': 'gestione separata',
eccetera.
}
------
DOCUMENTO

"""

def split_pdf(file_path, parts=2):
    """ Split a PDF into a specified number of equal parts """
    pdf_reader = PdfReader(file_path)
    num_pages = len(pdf_reader.pages)
    pages_per_part = max(1, num_pages // parts)
    output_files = []
    
    base_name = os.path.splitext(file_path)[0]

    for part in range(parts):
        start_page = part * pages_per_part
        end_page = min(start_page + pages_per_part, num_pages)
        if start_page >= num_pages:
            break
        pdf_writer = PdfWriter()
        for page_num in range(start_page, end_page):
            pdf_writer.add_page(pdf_reader.pages[page_num])
        
        output_filename = f"{base_name}_part{part + 1}.pdf"
        with open(output_filename, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
        
        output_files.append(output_filename)
        print(f"Split {file_path} into {output_filename} (Pages {start_page}-{end_page - 1})")

    return output_files

# Define the clean_and_format_json function
def clean_and_format_json(json_str):
    # Ensure the input is a string
    if not isinstance(json_str, str):
        raise ValueError("Input must be a string")
    
    # Step 1: Remove all quotes initially
    cleaned_json_str = re.sub(r'["\']', '', json_str)
    
    # Step 2: Add double quotes around keys (everything between { and :)
    cleaned_json_str = re.sub(r'({\s*|\s*,\s*)([^:{}]+?)(\s*:)', r'\1"\2"\3', cleaned_json_str)
    
    # Step 3: Add double quotes around values (everything between : and , or })
    cleaned_json_str = re.sub(r'(:\s*)([^,{}]+?)(\s*(,|}))', r'\1"\2"\3', cleaned_json_str)
    
    return cleaned_json_str

# Define the clean_response_text function
def clean_response_text(response_text):
    # Replace non-standard quotation marks with standard ones
    cleaned_response_text = response_text.replace('“', '"').replace('”', '"').replace("\\'", "'").replace('\\"', '"')
    
    # Remove the backticks and `python` identifier
    cleaned_response_text = cleaned_response_text.strip('```python').strip('```')

    # Normalize whitespace and remove newlines
    cleaned_response_text = cleaned_response_text.replace('\n', ' ').replace('\r', '')
    cleaned_response_text = re.sub(r'\s+', ' ', cleaned_response_text).strip()

    # Remove unnecessary escape characters
    cleaned_response_text = re.sub(r'\\([nrt])', r'\1', cleaned_response_text)
    cleaned_response_text = re.sub(r'\\{2,}', '', cleaned_response_text)
    
    # Extract JSON-like content from response_text
    json_content = re.search(r"\{.*?\}", cleaned_response_text, re.DOTALL)
    if json_content:
        json_str = json_content.group(0)
        
        # Clean and format the JSON string
        json_str = clean_and_format_json(json_str)
        
        return json_str

    return cleaned_response_text

# Define the process_json_string function
def process_json_string(json_str):
    try:
        json_data = json.loads(json_str)
        return json_data, None
    except json.JSONDecodeError as e:
        error_index = e.pos
        error_section = json_str[max(0, error_index-40):min(len(json_str), error_index+40)]
        return None, error_section

# Define the save_log function
def save_log(file_path, log_message):
    with open(file_path, 'a') as log_file:
        log_file.write(log_message + "\n")

# Define the process_file function
def process_file(file_path, file_index):
    project = "pftpro-167412"
    location = "us-central1"
    model_version = "gemini-1.5-flash"
    model = create_model(project, location, model_version)
    generation_config = {"max_output_tokens": MAX_TOKENS, "top_p": 0.95, "temperature": 0}

    all_dfs = []
    files_to_process = [file_path]

    while files_to_process:
        current_file = files_to_process.pop(0)

        for attempt in range(RETRY_LIMIT):
            try:
                # Preserve the initial prompt text
                prompt_example_4[:] = [text_6c_2]  # Preserve the initial text_6c_2

                mid_processing = get_file(current_file)  # Breakpoint here to inspect mid_processing

                if mid_processing:  # Ensure content is not empty
                    prompt_example_4.append(mid_processing)  # Breakpoint here to verify prompt_example_4 contents
                else:
                    print(f"Invalid content in mid_processing for file: {current_file}, type: {type(mid_processing)}")
                    return file_path, None

                test_response3 = model.generate_content(prompt_example_4, generation_config=generation_config)  # Breakpoint here to inspect test_response3

                response_text = test_response3.candidates[0].content.parts[0].text
                usage_metadata = test_response3.usage_metadata  # Corrected to access usage_metadata properly
                if usage_metadata.candidates_token_count >= MAX_TOKENS:  # Check token count if usage_metadata is available
                    # Split the file again and add the new parts to the processing list
                    split_files = split_pdf(current_file, parts=2)
                    files_to_process.extend(split_files)
                    break  # Break the retry loop and move to process the new split files

                # Clean the response text using the defined function
                cleaned_response_text = clean_response_text(response_text)

                # Remove any code block formatting
                cleaned_response_text = re.sub(r'```.*?```', '', cleaned_response_text, flags=re.DOTALL)

                # Replace single quotes with double quotes for valid JSON
                valid_json_str = cleaned_response_text.replace("'", '"')

                # Extract JSON-like content from response_text
                json_content = re.search(r"\{.*?\}", valid_json_str, re.DOTALL)
                if json_content:
                    json_str = json_content.group(0)
                    print(f"Extracted JSON string: {json_str}") 
                    
                    # Call the process_json_string function
                    funds_dict, error_section = process_json_string(json_str)
                    if funds_dict:
                        fund_names = list(funds_dict.keys())
                        print(f"Parsed fund names: {fund_names}")  
                    else:
                        # Highlight the specific section causing the error
                        print(f"JSON decoding error near: {error_section}")
                        fund_names = []
                else:
                    fund_names = []

                print(f"Extracted fund names from {file_path}: {fund_names}")
                
                if response_text and not fund_names:
                    pass

                if not fund_names:
                    return file_path, None  # Return the file path and None if no fund names found
                
                # Create DataFrame for the current file's fund names
                filename = os.path.basename(file_path)
                df = pd.DataFrame(fund_names, columns=['Fund Name'])
                df['File Name'] = filename
                all_dfs.append(df)
                
                # Save LLM Output with File Name
                with open(output_file_path, "a") as f:
                    f.write(f"############# {file_index} {filename} #############\n")
                    f.write(response_text + "\n\n")

                break  # Successfully processed, break the retry loop

            except (AttributeError, IndexError) as e:
                print(f"Error accessing text in {current_file}: {e}")
                return file_path, None  # Return the file path and None if an error occurs
            except Exception as e:
                if "503" in str(e):
                    print(f"Error processing file '{current_file}': {e}. Retrying in {RETRY_DELAY} seconds... (Attempt {attempt + 1} of {RETRY_LIMIT})")
                    time.sleep(RETRY_DELAY)
                else:
                    print(f"Error processing file '{current_file}': {e}")
                    return file_path, None  # Return the file path and None if any other error occurs

    if all_dfs:
        combined_df = pd.concat(all_dfs, ignore_index=True)
        excel_output_path = os.path.join(
            os.path.dirname(file_path).replace("micro_testing", "processing_test_flash_serial"), f"{os.path.basename(file_path).replace('.pdf', '.xlsx')}"
        )
        combined_df.to_excel(excel_output_path, index=False)
        print(f"Combined DataFrame saved to {excel_output_path}")

    return None, combined_df  # Return None and the combined DataFrame if processing was successful

def main():
    directory = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\micro_testing"
    files_to_process = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.pdf')]
    
    unprocessed_files = []
    all_dataframes = []
    response_count = 0
    
    for file_index, file_path in enumerate(files_to_process, start=1):
        pdf_reader = PdfReader(file_path)
        num_pages = len(pdf_reader.pages)
        
        if num_pages > MAX_PAGES:
            split_files = split_pdf(file_path, parts=2)  # Breakpoint here to check if the file is split
        else:
            split_files = [file_path]
        
        for split_file_path in split_files:
            result = process_file(split_file_path, file_index)  # Breakpoint here to debug process_file function
            if result[0] is not None:
                unprocessed_files.append(result[0])
            if result[1] is not None:
                all_dataframes.append(result[1])
                response_count += 1
    
    if unprocessed_files:
        print("The following files were not processed successfully:")
        for file in unprocessed_files:
            print(file)
    else:
        print("All files processed successfully.")

    # Combine all dataframes into one and save to a single Excel file
    if all_dataframes:
        combined_df = pd.concat(all_dataframes, ignore_index=True)
        combined_df.to_excel(combined_excel_output_path, index=False)
        print(f"Combined results saved to {combined_excel_output_path}")
    
    # Append the response count to the output file
    with open(output_file_path, "a") as f:
        f.write(f"\nTotal LLM Responses Saved: {response_count}\n")

if __name__ == "__main__":
    main()

