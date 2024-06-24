import pandas as pd
import openpyxl
def generate_data():
    data = [
        {"First Name": "John", "Last Name": "Doe", "Email": "john.doe@example.com", "Phone Number": "555-1234"},
        {"First Name": "Jane", "Last Name": "Smith", "Email": "jane.smith@example.com", "Phone Number": "555-5678"},
        {"First Name": "Michael", "Last Name": "Johnson", "Email": "michael.johnson@example.com", "Phone Number": "555-8765"},
        {"First Name": "Emily", "Last Name": "Davis", "Email": "emily.davis@example.com", "Phone Number": "555-4321"}
    ]
    return data

# Generate data using the function
data = generate_data()

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel("contacts.xlsx", index=False)
