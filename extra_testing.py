

# import pandas as pd

# # Load the Excel file
# file_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\combined_results.xlsx"
# combined_df = pd.read_excel(file_path)

# # Get distinct file names
# distinct_file_names = combined_df['File Name'].unique()

# # Print the number of distinct file names
# print(f"Number of distinct file names: {len(distinct_file_names)}")

# # Print the distinct file names
# print("Distinct file names:")
# for file_name in distinct_file_names:
#     print(file_name)


######################### checking accuracy
# import pandas as pd

# # Define file paths
# combined_results_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\combined_results.xlsx"
# gen_ai_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\GEN_AI_Estrazione_sottostanti IBIPS.xlsx"

# # Load the Excel files
# combined_results_df = pd.read_excel(combined_results_path)
# gen_ai_df = pd.read_excel(gen_ai_path, sheet_name="Sottostanti da estrarre con AI")

# # Print columns to understand the structure
# print("Columns in combined_results_df:")
# print(combined_results_df.columns)

# print("Columns in gen_ai_df:")
# print(gen_ai_df.columns)

# # Normalize the columns by stripping spaces and converting to lowercase
# combined_results_df['File Name'] = combined_results_df['File Name'].astype(str).str.strip().str.lower()
# gen_ai_df['Nome FILE'] = gen_ai_df['Nome FILE'].astype(str).str.strip().str.lower()

# # Initialize a list to store the results
# results = []

# # Perform exact matching and collect the results
# for i, row in combined_results_df.iterrows():
#     file_name = row['File Name']
#     matched_row = gen_ai_df[gen_ai_df['Nome FILE'] == file_name]
    
#     if not matched_row.empty:
#         gen_ai_fund_name = matched_row.iloc[0, 5]  # 5th index column (6th from start)
#         combined_results_fund_name = row['Fund Name']
#         results.append([file_name, combined_results_fund_name, gen_ai_fund_name])
#         combined_results_df.at[i, 'Score'] = 1
#     else:
#         combined_results_df.at[i, 'Score'] = 0

# # Create a DataFrame for the results
# results_df = pd.DataFrame(results, columns=['File Name', 'Fund Name from combined_results.xlsx', 'Fund Name from GEN_AI_Estrazione_sottostanti_IBIPS.xlsx'])

# # Save the results to a new Excel file
# output_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\matched_results_exact.xlsx"
# results_df.to_excel(output_path, index=False)

# # Save the updated combined_results_df with scores
# combined_results_output_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\combined_results_with_scores33333.xlsx"
# combined_results_df.to_excel(combined_results_output_path, index=False)

# print(f"Matched results saved to: {output_path}")
# print(f"Combined results with scores saved to: {combined_results_output_path}")

##########################################
import pandas as pd
from fuzzywuzzy import fuzz

# Define file paths
combined_results_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\combined_results_test_serialDB.xlsx"
ground_truth_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\GroundTruth.xlsx"

# Load the Excel files without skipping any rows
combined_results_df = pd.read_excel(combined_results_path)
ground_truth_df = pd.read_excel(ground_truth_path, sheet_name=0)

# Normalize only the Fund Name and Nome Sottostante columns by stripping spaces and converting to lowercase
combined_results_df.iloc[:, 0] = combined_results_df.iloc[:, 0].astype(str).str.strip().str.lower()  # Fund Name
ground_truth_df.iloc[:, 5] = ground_truth_df.iloc[:, 5].astype(str).str.strip().str.lower()  # Nome Sottostante

# Debugging: Print samples to check for issues
print("Combined Results 'File Name' sample:\n", combined_results_df.iloc[:, 1].head())
print("Combined Results 'Fund Name' sample:\n", combined_results_df.iloc[:, 0].head())
print("Ground Truth 'Nome FILE' sample:\n", ground_truth_df.iloc[:, 0].head())
print("Ground Truth 'Nome Sottostante' sample:\n", ground_truth_df.iloc[:, 5].head())

# Create a new DataFrame to store the results
results = []

# Perform the fuzzy matching and store similarity scores
for file_name, fund_name in zip(combined_results_df.iloc[:, 1], combined_results_df.iloc[:, 0]):
    relevant_rows = ground_truth_df[ground_truth_df.iloc[:, 0] == file_name]
    
    # Debugging: Print relevant rows to check filtering
    if relevant_rows.empty:
        print(f"No match found for file name '{file_name}'.")
    else:
        print(f"Relevant rows for file name '{file_name}':\n", relevant_rows)
    
    max_similarity = 0
    best_match = None
    for nome_sottostante in relevant_rows.iloc[:, 5]:
        print(f"Comparing Fund Name '{fund_name}' with Nome Sottostante '{nome_sottostante}'")
        similarity = fuzz.ratio(fund_name, nome_sottostante)
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = nome_sottostante

    if best_match is not None:
        results.append([file_name, fund_name, best_match, max_similarity])

# Create a DataFrame for the results
results_df = pd.DataFrame(results, columns=['File Name', 'Fund Name', 'Best Match Nome Sottostante', 'Similarity Score'])

# Save the results to a new Excel file
output_path = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\matched_results_max_similarity1.xlsx"
results_df.to_excel(output_path, index=False)

print(f"Updated file saved to: {output_path}")




