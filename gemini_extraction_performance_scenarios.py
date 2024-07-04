##################################### Gemini extraction, single file
from models.gemini.gemini_multimodal import get_file, create_model
from extractors.models import Models
from extractors.general_extractors.config.prompt_config import table_schemas
from AWSInteraction.EnvVarSetter import EnvVarSetter
import json
import pandas as pd
from typing import List
from pydantic import BaseModel, Field
from typing import Optional
import os

# Initialize and set environment variables
env_setter = EnvVarSetter()
env_setter.configure_local_env_vars()

NF = "not found"
NA = "N/A"

# Load the example prompts
from prompts.certificates.test_prompt_complexity.example_prompt_1 import prompt_example_1, prompt_example_3, prompt_example_2

# Create the generative model
project="pftpro-167412"
location="us-central1"
model_version = "gemini-1.5-pro-preview-0409"
model = create_model(project, location, model_version)

# Configuration for the generation
generation_config = {
    "max_output_tokens": 800,
    "top_p": 0.95,
    "temperature": 0,
}

schema1 = "general_info"
schema2 = "gemini"
file_id = "random string"

def extract_info1(text, general_schema, file_id):
    pydantic_class = table_schemas["it"][general_schema]
    print(pydantic_class)
    extraction = Models.tag(text.text, pydantic_class, file_id)
    return extraction

def extract_info2(text, general_schema, file_id):
    pydantic_class = gemini_schema["it"][general_schema]
    print(pydantic_class)
    extraction = Models.tag(text.text, pydantic_class, file_id)
    return extraction

# 2 - LOAD THE OBJECTIVE FILE
test_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_PerformanceScenario_Extraction\PRODOTTI\CNP UNICREDIT VITA\202305_CNP Azionario Trend Futuri_My Vision.pdf"
IST_path = r"C:\Users\ribhu.kaul\RibhuLLM\Gemini_Extraction\Population2.pdf"                         

# Extract the filename from the path
filename = os.path.basename(test_path)

# 3 - ADD THE OBJECTIVE FILE TO THE PROMPT
test = get_file(test_path)
print(type(test))
prompt_example_3.append(test)

# GENERATE THE RESULT
test_response = model.generate_content(prompt_example_3, generation_config=generation_config)
print(test_response)

# Extract the text content from the response
response_text = test_response.candidates[0].content.parts[0].text

# Save response to a text file
response_file_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_PerformanceScenario_Extraction\LLM_response2.txt"
with open(response_file_path, 'w', encoding='utf-8') as f:
    f.write(response_text)

text = test_response

var1 = extract_info1(text, schema1, file_id)
print(var1)
# Extract the attributes
data1 = {
    "indicatore_sintetico_rischio": var1.indicatore_sintetico_rischio,
    "periodo_detenzione_raccomandato": var1.periodo_detenzione_raccomandato,
    "date": var1.date
}

rhp = data1["periodo_detenzione_raccomandato"]
print(rhp)

class GeminiExtraction1(BaseModel):
    scenario_moderato: str = Field(NF, description= "Rendimento percentuale(%) o '-'  1 anno scenario moderato")
    scenario_moderato_rhp: str = Field(NF, description= f"Rendimento percentuale(%) o '-' {rhp} anni scenario moderato")
    impatto_dei_costi: str = Field(NF, description= "Impatto sui costi annuali in % per uscita dopo 1 anno")
    impatto_dei_costi_rhp : str = Field(NF,description= f"Impatto sui costi annuali in % per uscita dopo {rhp} anno")

gemini_schema = {
    "it":{
        "gemini": GeminiExtraction1
    }
}

var2 = extract_info2(text, general_schema=schema2, file_id=file_id)
print(var2)

data2 = {
    "moderato_return": var2.scenario_moderato,
    "moderato_return_rhp": var2.scenario_moderato_rhp,
    "incidenza_annua": var2.impatto_dei_costi,
    "incidenza_annua_rhp": var2. impatto_dei_costi_rhp    
}

# Convert the dictionary to a pandas DataFrame
df1 = pd.DataFrame([data1])
df2 = pd.DataFrame([data2])

# Add the filename as the first column in both DataFrames
df1.insert(0, 'filename', filename)
df2.insert(0, 'filename', filename)

print(df1)
print(df2)
# Specify the path where you want to save the Excel file
# excel_output_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\extracted_info1.xlsx"

# # Save both DataFrames to separate sheets in the same Excel file
# with pd.ExcelWriter(excel_output_path) as writer:
#     df1.to_excel(writer, sheet_name='Sheet1', index=False)
#     df2.to_excel(writer, sheet_name='Sheet2', index=False)

# Optionally, you can also handle ISTAT files as needed
# ist1 = get_file(IST_path)
# print(type(ist1))
# prompt_example_3.append(ist1)
# ist1_response = model.generate_content(prompt_example_3, generation_config=generation_config)
# print(ist1_response)

######################################## ISTAT checking  not willing to extract 

# ist1 = get_file(IST_path)
# print(type(ist1))
# prompt_example_3.append(ist1)

# ist1_response = model.generate_content(prompt_example_3, generation_config=generation_config)
# print(ist1_response)



##################################################################################
# MULTIPLE FILE PARALLEL PROCESSING INCLUDING  total_token_count & saving in excel 

# import os
# import pandas as pd
# from concurrent.futures import ThreadPoolExecutor, as_completed
# from models.gemini.gemini_multimodal import get_file, create_model
# from extractors.models import Models
# from extractors.general_extractors.config.prompt_config import table_schemas
# from AWSInteraction.EnvVarSetter import EnvVarSetter
# from pydantic import BaseModel, Field

# # Initialize and set environment variables
# env_setter = EnvVarSetter()
# env_setter.configure_local_env_vars()

# NF = "not found"
# NA = "N/A"

# # Load the example prompts
# from prompts.certificates.test_prompt_complexity.example_prompt_1 import prompt_example_1, prompt_example_2, prompt_example_3

# # Create the generative model
# project = "pftpro-167412"
# location = "us-central1"
# model_version = "gemini-1.5-pro-preview-0409"
# model = create_model(project, location, model_version)

# # Configuration for the generation
# generation_config = {
#     "max_output_tokens": 800,
#     "top_p": 0.95,
#     "temperature": 0,
# }

# schema1 = "general_info"
# schema2 = "gemini"
# file_id = "random string"

# def extract_info1(text, general_schema, file_id):
#     pydantic_class = table_schemas["it"][general_schema]
#     extraction = Models.tag(text.text, pydantic_class, file_id)
#     return extraction

# def extract_info2(text, general_schema, file_id):
#     pydantic_class = gemini_schema["it"][general_schema]
#     extraction = Models.tag(text.text, pydantic_class, file_id)
#     return extraction

# def process_file(filename):
#     file_path = os.path.join(input_directory, filename)
#     print(file_path)

#     # Read the file
#     test = get_file(file_path)
#     print(test)

#     # Update the prompt with the file content
#     local_prompt = prompt_example_2.copy()  # Create a local copy of the prompt to avoid thread conflicts
#     local_prompt.append(test)

#     # Generate the response
#     test_response = model.generate_content(local_prompt, generation_config=generation_config)
#     text = test_response
#     print(text)

#     # Extract total_token_count from usage_metadata
#     total_token_count = text.usage_metadata.total_token_count

#     # Extract information using schema1
#     var1 = extract_info1(text, schema1, file_id)
#     data1 = {
#         "indicatore_sintetico_rischio": var1.indicatore_sintetico_rischio,
#         "periodo_detenzione_raccomandato": var1.periodo_detenzione_raccomandato,
#         "date": var1.date,
#         "filename": filename,
#         "total_token_count": total_token_count
#     }

#     rhp = data1["periodo_detenzione_raccomandato"]

#     # Define the GeminiExtraction1 class dynamically
#     class GeminiExtraction1(BaseModel):
#         scenario_moderato: str = Field(NF, description="Rendimento percentuale(%) o '-' 1 anno scenario moderato")
#         scenario_moderato_rhp: str = Field(NF, description=f"Rendimento percentuale(%) a {rhp} anni scenario moderato")
#         impatto_dei_costi: str = Field(NF, description="Impatto sui costi annuali in % per uscita dopo 1 anno")
#         impatto_dei_costi_rhp: str = Field(NF, description=f"Impatto sui costi annuali in % per uscita dopo {rhp} anno")

#     global gemini_schema  # Define gemini_schema as global to access within the function
#     gemini_schema = {
#         "it": {
#             "gemini": GeminiExtraction1
#         }
#     }

#     # Extract information using schema2
#     var2 = extract_info2(text, schema2, file_id)
#     data2 = {
#         "moderato_return": var2.scenario_moderato,
#         "moderato_return_rhp": var2.scenario_moderato_rhp,
#         "incidenza_annua": var2.impatto_dei_costi,
#         "incidenza_annua_rhp": var2.impatto_dei_costi_rhp,
#         "filename": filename,
#         "total_token_count": total_token_count
#     }

#     return data1, data2

# # Directory containing input files
# input_directory = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\input_files_matched"

# # Lists to store extracted data
# data1_list = []
# data2_list = []

# # Using ThreadPoolExecutor to process files in parallel
# with ThreadPoolExecutor(max_workers=5) as executor:
#     futures = [executor.submit(process_file, filename) for filename in os.listdir(input_directory) if filename.endswith(".pdf")]
#     for future in as_completed(futures):
#         try:
#             result = future.result()
#             data1_list.append(result[0])
#             data2_list.append(result[1])
#         except Exception as e:
#             print(f"Error processing file: {e}")

# # Convert lists to DataFrames
# df1 = pd.DataFrame(data1_list)
# df2 = pd.DataFrame(data2_list)

# # Specify the path where you want to save the Excel file
# excel_output_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\extracted_info2PRLT_CR1.xlsx"

# # Save both DataFrames to separate sheets in the same Excel file
# with pd.ExcelWriter(excel_output_path) as writer:
#     df1.to_excel(writer, sheet_name='Sheet1', index=False)
#     df2.to_excel(writer, sheet_name='Sheet2', index=False)


###################################################################################################
# MULTIPLE FILE PARALLEL PROCESSING INCLUDING  total_token_count & saving in excel & saving LLM output in a txt file

# import os
# import pandas as pd
# from concurrent.futures import ThreadPoolExecutor, as_completed
# from models.gemini.gemini_multimodal import get_file, create_model
# from extractors.models import Models
# from extractors.general_extractors.config.prompt_config import table_schemas
# from AWSInteraction.EnvVarSetter import EnvVarSetter
# from pydantic import BaseModel, Field

# # Initialize and set environment variables
# env_setter = EnvVarSetter()
# env_setter.configure_local_env_vars()

# NF = "not found"
# NA = "N/A"

# # Load the example prompts
# from prompts.certificates.test_prompt_complexity.example_prompt_1 import prompt_example_1, prompt_example_2, prompt_example_3

# # Create the generative model
# project = "pftpro-167412"
# location = "us-central1"
# model_version = "gemini-1.5-pro-preview-0409"
# model = create_model(project, location, model_version)

# # Configuration for the generation
# generation_config = {
#     "max_output_tokens": 800,
#     "top_p": 0.95,
#     "temperature": 0,
# }

# schema1 = "general_info"
# schema2 = "gemini"
# file_id = "random string"

# def extract_info1(text, general_schema, file_id):
#     pydantic_class = table_schemas["it"][general_schema]
#     extraction = Models.tag(text.text, pydantic_class, file_id)
#     return extraction

# def extract_info2(text, general_schema, file_id):
#     pydantic_class = gemini_schema["it"][general_schema]
#     extraction = Models.tag(text.text, pydantic_class, file_id)
#     return extraction

# def process_file(filename):
#     file_path = os.path.join(input_directory, filename)
#     print(file_path)

#     # Read the file
#     test = get_file(file_path)
#     print(test)

#     # Update the prompt with the file content
#     local_prompt = prompt_example_3.copy()  # Create a local copy of the prompt to avoid thread conflicts
#     local_prompt.append(test)

#     # Generate the response
#     test_response = model.generate_content(local_prompt, generation_config=generation_config)
#     text = test_response
#     print(text)

#     # Extract total_token_count from usage_metadata
#     total_token_count = text.usage_metadata.total_token_count

#     # Extract the text content from the response
#     response_text = test_response.candidates[0].content.parts[0].text

#     # Save response to a text file
#     response_file_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\LLM_response.txt"
#     with open(response_file_path, 'a', encoding='utf-8') as f:
#         f.write(f"############ {filename}\n")
#         f.write(response_text + '\n')

#     # Extract information using schema1
#     var1 = extract_info1(text, schema1, file_id)
#     data1 = {
#         "indicatore_sintetico_rischio": var1.indicatore_sintetico_rischio,
#         "periodo_detenzione_raccomandato": var1.periodo_detenzione_raccomandato,
#         "date": var1.date,
#         "filename": filename,
#         "total_token_count": total_token_count
#     }

#     rhp = data1["periodo_detenzione_raccomandato"]

#     # Define the GeminiExtraction1 class dynamically
#     class GeminiExtraction1(BaseModel):
#         scenario_moderato: str = Field(NF, description="Rendimento percentuale(%) o '-' 1 anno scenario moderato")
#         scenario_moderato_rhp: str = Field(NF, description=f"Rendimento percentuale(%) a {rhp} anni scenario moderato")
#         impatto_dei_costi: str = Field(NF, description="Impatto sui costi annuali in % per uscita dopo 1 anno")
#         impatto_dei_costi_rhp: str = Field(NF, description=f"Impatto sui costi annuali in % per uscita dopo {rhp} anno")

#     global gemini_schema  # Define gemini_schema as global to access within the function
#     gemini_schema = {
#         "it": {
#             "gemini": GeminiExtraction1
#         }
#     }

#     # Extract information using schema2
#     var2 = extract_info2(text, schema2, file_id)
#     data2 = {
#         "moderato_return": var2.scenario_moderato,
#         "moderato_return_rhp": var2.scenario_moderato_rhp,
#         "incidenza_annua": var2.impatto_dei_costi,
#         "incidenza_annua_rhp": var2.impatto_dei_costi_rhp,
#         "filename": filename,
#         "total_token_count": total_token_count
#     }

#     return data1, data2

# # Directory containing input files
# input_directory = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\input_files_matched"

# # Lists to store extracted data
# data1_list = []
# data2_list = []

# # Using ThreadPoolExecutor to process files in parallel
# with ThreadPoolExecutor(max_workers=5) as executor:
#     futures = [executor.submit(process_file, filename) for filename in os.listdir(input_directory) if filename.endswith(".pdf")]
#     for future in as_completed(futures):
#         try:
#             result = future.result()
#             data1_list.append(result[0])
#             data2_list.append(result[1])
#         except Exception as e:
#             print(f"Error processing file: {e}")

# # Convert lists to DataFrames
# df1 = pd.DataFrame(data1_list)
# df2 = pd.DataFrame(data2_list)

# # Specify the path where you want to save the Excel file
# excel_output_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\extracted_info2PRLT_CR2_W_LMOP.xlsx"

# # Save both DataFrames to separate sheets in the same Excel file
# with pd.ExcelWriter(excel_output_path) as writer:
#     df1.to_excel(writer, sheet_name='Sheet1', index=False)
#     df2.to_excel(writer, sheet_name='Sheet2', index=False)
