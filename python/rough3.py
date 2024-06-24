import pandas as pd

# Define the file paths
file1_path = "data.xlsx"
file2_path = "data2.xlsx"
output_path = "merged_file.xlsx"

try:
    # Read specific columns from each Excel file into DataFrames
    df1 = pd.read_excel(file1_path, usecols=["employee_id"]) 
     # Replace with your column names
    df2 = pd.read_excel(file2_path, usecols=["predicted_employee_id"])  # Replace with your column names

    # Combine the DataFrames side by side (column-wise)
    merged_df = pd.concat([df1, df2], axis=1)

    # Save the merged DataFrame to a new Excel file
    merged_df.to_excel(output_path, index=False)

    print(f"Columns from {file1_path} and {file2_path} merged successfully into {output_path}")

except PermissionError as e:
    print(f"PermissionError: {e}. Ensure the file is not open in any other program and you have the necessary permissions.")
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}. Ensure the file path is correct.")
except Exception as e:
    print(f"An error occurred: {e}")
