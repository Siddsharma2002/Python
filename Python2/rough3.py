import pandas as pd
import Levenshtein

# Load data from the first Excel file
df1 = pd.read_excel('data1.xlsx')
# Load data from the second Excel file
df2 = pd.read_excel('data2.xlsx')

# Assuming the data to be compared is in the first column of each file
column1 = df1.iloc[:, 0]
column2 = df2.iloc[:, 0]

# List to store the results
results = []

# Calculate Levenshtein distance for each pair of strings
for str1 in column1:
    for str2 in column2:
        distance = Levenshtein.distance(str1, str2)
        results.append({'String1': str1, 'String2': str2, 'Levenshtein Distance': distance})

# Convert the results list to a DataFrame
results_df = pd.DataFrame(results)

# Save the results to a new Excel file
results_df.to_excel('levenshtein_results.xlsx', index=False)

print('Levenshtein distances have been calculated and saved to levenshtein_results.xlsx')
