import pandas as pd
# You can use openpyxl or xlsxwriter for more control over formatting
# This is a basic example using pandas to create a simple Excel file

def generate_excel_report():
    data = {'Column A': [1, 2, 3], 'Column B': [4, 5, 6]}
    df = pd.DataFrame(data)
    output_filename = 'Generated_Report.xlsx'
    df.to_excel(output_filename, index=False, engine='xlsxwriter') # Use xlsxwriter engine
    print(f"Created report: {output_filename}")

if __name__ == "__main__":
    generate_excel_report()
