# scripts/generate_report.py
import pandas as pd
import os

# Sample data
data = {'TC#': [1, 2, 3, 4],
        'TestCaseName': ['test_CreateUser', 'test_CreateuserOffersName', 'test_getuser', 'test_UpdateUser']}
df = pd.DataFrame(data)

# Define the output path
output_dir = 'reports'
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'Execution-Status-Report.xlsx')

# Generate the Excel report
df.to_excel(output_file, index=False, sheet_name='Report Data')
print(f'Generated report: {output_file}')
