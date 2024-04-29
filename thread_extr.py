from concurrent.futures import ThreadPoolExecutor, as_completed
from extractors.custom_extractors.wamasset.kidtable import WamassetKidTableextractor
from AWSInteraction.EnvVarSetter import EnvVarSetter
import pandas as pd
import os

# Set up environment variables
env_setter = EnvVarSetter()
env_setter.configure_local_env_vars()

# Load the Excel file for file names and types
excel_path = "C:/Users/simone.mugnai/Desktop/Fees_Fondi_GenAi_new (1).xlsm"
df = pd.read_excel(excel_path, usecols='A:B')

# Filter to get filenames where the type is 'KID'
kid_files = df[df['KID/KIID'] == 'KID']['Nome documento'].tolist()

pdf_directory = 'data_test/priipkid'

# Function to process each PDF and return the result as a DataFrame
def process_pdf(file_name):
    file_path = os.path.join(pdf_directory, file_name)
    try:
        extractor = WamassetKidTableextractor(file_path)
        result_df = extractor.process()  # Assume this function now returns a DataFrame
        result_df['Filename'] = file_name  # Add a column for the file name
        return result_df
    except Exception as e:
        print(f"Error processing {file_name}: {str(e)}")
        return pd.DataFrame()  # Return an empty DataFrame in case of an error

# Function to handle threading of PDF processing
def process_files_concurrently(file_names):
    final_results_df = pd.DataFrame()
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Submit all PDF processing tasks concurrently
        future_to_file = {executor.submit(process_pdf, file): file for file in file_names}
        for future in as_completed(future_to_file):
            file_result_df = future.result()
            if not file_result_df.empty:
                final_results_df = pd.concat([final_results_df, file_result_df], axis=0, ignore_index=True)
    return final_results_df

# Process all files concurrently and collect results
final_results_df = process_files_concurrently(kid_files)

# Drop every second row from the results DataFrame
indices_to_drop = range(2, len(final_results_df), 2)
final_results_df = final_results_df.drop(indices_to_drop).reset_index(drop=True)

# Save the concatenated results to an Excel file
final_results_df.to_excel('C:/Users/simone.mugnai/Desktop/please_eval_ouput.xlsx', index=False)
