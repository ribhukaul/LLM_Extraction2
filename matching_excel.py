import pandas as pd

def compare_excel_files(file1, file2, output_file):
    # Load the first file
    df1 = pd.read_excel(file1)
    
    # Load the second file
    df2 = pd.read_excel(file2)
    
    # Merge both files on the "Nome documento" column, keeping only the rows that appear in both dataframes
    result_df = pd.merge(df1, df2, on="Nome documento")
    
    # Save the merged data to a new Excel file
    result_df.to_excel(output_file, index=False)
    print(f"Saved matched rows to {output_file}")

# Example usage
file1_path = 'evaluation_output.xlsx'  # Update with your first file path
file2_path = 'data_test\Fees_Fondi_GenAi_new.xlsm'  # Update with your second file path
output_path = 'output.xlsx'  # Define your output file name

compare_excel_files(file1_path, file2_path, output_path)

