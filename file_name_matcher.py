# ###################################### This code works fine in choosing files
# import pandas as pd
# import os
# import shutil

# # Paths configuration
# excel_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\UNIT LINKED (2).xlsx"
# source_folder = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\input_files"
# destination_folder = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\input_files_matched"

# # Ensure the destination directory exists
# if not os.path.exists(destination_folder):
#     os.makedirs(destination_folder)

# # Load the Excel file, skipping the first 2 rows (index starts from 0)
# df = pd.read_excel(excel_path, skiprows=2)

# # Print the first few rows of the dataframe to ensure it's loading data correctly
# print("Loaded DataFrame head:")
# print(df.head())

# # Define the possible file extensions
# extensions = ['.pdf', '.docx', '.xlsx', '.txt']

# # Loop through the specified rows and try to find and copy the files with any of the listed extensions
# for i in range(80):  # Adjust range as necessary
#     base_file_name = df.iloc[i, 1]  # Assuming names are in column 2 (index 1)
#     print(f"Checking for file: {base_file_name}")  # Debugging print statement

#     file_found = False
#     for ext in extensions:
#         file_name_with_ext = f"{base_file_name}{ext}"
#         file_path = os.path.join(source_folder, file_name_with_ext)
        
#         print(f"Looking for: {file_path}")  # Debugging print statement
        
#         if os.path.exists(file_path):
#             print(f"Found file: {file_path}")  # Confirm when files are found
#             shutil.copy(file_path, destination_folder)
#             file_found = True
#             break
    
#     if not file_found:
#         print(f"File not found: {base_file_name} with any supported extension")

# # Additional debugging: List all files in the source directory
# print("Files available in the directory:")
# print(os.listdir(source_folder))

# print("Operation completed.")

#####################################################
# import pandas as pd
# import os
# import shutil

# # Paths configuration
# excel_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\UNIT LINKED (2).xlsx"
# source_folder = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\input_files"
# destination_folder = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\input_files_matched"

# # Ensure the destination directory exists
# if not os.path.exists(destination_folder):
#     os.makedirs(destination_folder)

# # Load the Excel file, skipping the first 2 rows (index starts from 0)
# df = pd.read_excel(excel_path, skiprows=2)

# # Print the first few rows of the dataframe to ensure it's loading data correctly
# print("Loaded DataFrame head:")
# print(df.head())

# # Define the possible file extensions
# extensions = ['.pdf', '.docx', '.xlsx', '.txt']

# # List to hold names of files that were not found
# not_found_files = []

# # Loop through the specified rows and try to find and copy the files with any of the listed extensions
# for i in range(80):  # Adjust range as necessary
#     base_file_name = df.iloc[i, 1]  # Assuming names are in column 2 (index 1)
#     print(f"Checking for file: {base_file_name}")  # Debugging print statement

#     file_found = False
#     for ext in extensions:
#         file_name_with_ext = f"{base_file_name}{ext}"
#         file_path = os.path.join(source_folder, file_name_with_ext)
        
#         print(f"Looking for: {file_path}")  # Debugging print statement
        
#         if os.path.exists(file_path):
#             print(f"Found file: {file_path}")  # Confirm when files are found
#             shutil.copy(file_path, destination_folder)
#             file_found = True
#             break
    
#     if not file_found:
#         print(f"File not found: {base_file_name} with any supported extension")
#         not_found_files.append(base_file_name)

# # Additional debugging: List all files in the source directory
# print("Files available in the directory:")
# print(os.listdir(source_folder))

# # Print files that were not found
# print("Files not found (total of {}):".format(len(not_found_files)))
# for file in not_found_files:
#     print(file)

# print("Operation completed.")
###################################################

# # code for matching files from the ground truth excel and the extraced excel, further matching for accuracy calculation is required
# import pandas as pd

# # File paths
# file1_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\UNIT LINKED (2).xlsx"
# file2_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\extracted_info2PRLT.xlsx"
# output_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\matched_comparison.xlsx"

# # Read the Excel files
# df1 = pd.read_excel(file1_path)
# df2_sheet1 = pd.read_excel(file2_path, sheet_name=0)
# df2_sheet2 = pd.read_excel(file2_path, sheet_name=1)

# # Lists to store matched rows
# matched_rows1 = []
# matched_rows2_sheet1 = []
# matched_rows2_sheet2 = []

# # Loop to compare entries and store matched rows
# for i in range(81):
#     entry1 = df1.iloc[i, 5]  # Assuming the column for comparison is the 6th column in df1 (ISIN)
#     entry2 = df2_sheet1.iloc[i, 0]  # Assuming the column for comparison is the 1st column in df2_sheet1
    
#     if entry1 == entry2:
#         matched_rows1.append(df1.iloc[i])
#         matched_rows2_sheet1.append(df2_sheet1.iloc[i])
#         matched_rows2_sheet2.append(df2_sheet2.iloc[i])

# # Convert matched rows to DataFrames
# matched_df1 = pd.DataFrame(matched_rows1)
# matched_df2_sheet1 = pd.DataFrame(matched_rows2_sheet1)
# matched_df2_sheet2 = pd.DataFrame(matched_rows2_sheet2)

# # Write the matched rows to a new Excel file
# with pd.ExcelWriter(output_path) as writer:
#     matched_df1.to_excel(writer, sheet_name='Matched_Unit_Linked', index=False)
#     matched_df2_sheet1.to_excel(writer, sheet_name='Matched_Extracted_Sheet1', index=False)
#     matched_df2_sheet2.to_excel(writer, sheet_name='Matched_Extracted_Sheet2', index=False)

# print(f"Matched entries have been written to {output_path}")
########################################################################



