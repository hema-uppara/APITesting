# scripts/generate_report.py
import pandas as pd
import os

# Sample data
data = {'Column A': [1, 2, 3, 4],
        'Column B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Define the output path
output_dir = 'reports'
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'automated_report.xlsx')

# Generate the Excel report
df.to_excel(output_file, index=False, sheet_name='Report Data')
print(f'Generated report: {output_file}')
