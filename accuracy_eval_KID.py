from extractors.custom_extractors.wamasset.kidtable import WamassetKidTableextractor
from AWSInteraction.EnvVarSetter import EnvVarSetter
import pandas as pd
import os

env_setter = EnvVarSetter()
env_setter.configure_local_env_vars()

# Load the Excel file for file names and types
excel_path = 'data_test/Fees_Fondi_GenAi_new.xlsm'
df = pd.read_excel(excel_path, usecols='A:B')

# Filter to get filenames where the type is 'KID'
kid_files = df[df['KID/KIID'] == 'KID']['Nome documento'].tolist()

#select specific document 
#kid_files = df[df['Nome documento'] == 'priipkid_LU0828344357.pdf'].tolist()


#kid_files = kid_files[:8]



pdf_directory = 'data_test/priipkid'

# Function to process each PDF and return the result as a DataFrame
def process_pdf(file_name):
    file_path = os.path.join(pdf_directory, file_name)
    try:
        extractor = WamassetKidTableextractor(file_path)
        result_df = extractor.process()  # The process now handles DataFrame creation internally
        return result_df
    except Exception as e:
        print(f"Error processing {file_name}: {str(e)}")
        return pd.DataFrame()  # Return an empty DataFrame in case of an error

# Initialize an empty DataFrame for results
final_results_df = pd.DataFrame()

# Loop through each filtered filename and process it
for file in kid_files:
    file_result_df = process_pdf(file)
    if not file_result_df.empty:  # Only add non-empty results
        print(file)
        file_result_df['Filename'] = file  # Add a column for the file name
        final_results_df = pd.concat([final_results_df, file_result_df], axis=0, ignore_index=True)

# Calculate the indices of the rows you want to drop
indices_to_drop = range(2, len(final_results_df), 2)

# Drop the rows from the DataFrame
final_results_df = final_results_df.drop(indices_to_drop).reset_index(drop=True)


# Save the concatenated results to an Excel file
final_results_df.to_excel('C:/Users/simone.mugnai/Desktop/third_eval_ouput.xlsx', index=False)


