import pandas as pd

def compare_excel_files(file1, file2, output_file):
    # Load the first file
    df1 = pd.read_excel(file1)
    
    # Load the second file
    df2 = pd.read_excel(file2)

    # Convert all columns to numeric if possible, errors='ignore' will leave non-convertible columns unchanged
    df1 = df1.apply(pd.to_numeric, errors='ignore')
    df2 = df2.apply(pd.to_numeric, errors='ignore')

    # Identify common columns including the 'Nome documento' for merging
   
    
    # Merge both files on the "Nome documento" columns, keeping only the rows and columns that appear in both dataframes
    result_df = pd.merge(df1, df2, on="Nome documento")
    
    
    # Save the merged data to a new Excel file
    result_df.to_excel(output_file, index=False)
    print(f"Saved matched rows to {output_file}")

# Example usage
file1_path = 'C:/Users/simone.mugnai/Desktop/please_eval_ouput.xlsx'  # Update with your first file path
file2_path = 'C:/Users/simone.mugnai/Desktop/Fees_Fondi_GenAi_new (1).xlsm'  # Update with your second file path
output_path = 'output2.xlsx'  # Define your output file name

compare_excel_files(file1_path, file2_path, output_path)

