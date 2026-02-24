import openpyxl
import os

def create_excel_report():
    # Create a new Excel workbook and select the active sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Execution Status Report" #

    # Add headers
    sheet['A1'] = 'Task'
    sheet['B1'] = 'Owner'
    sheet['C1'] = 'Status'
    sheet['D1'] = 'Notes'

    # Add some dummy data (replace with actual dynamic data from your workflow context)
    data = [
        ['Build Code', 'Team A', 'On Track', 'Build completed successfully'],
        ['Run Tests', 'Team B', 'Potential Risk', 'Some tests are flaky'],
        ['Deploy to Staging', 'Team C', 'Roadblock', 'Permissions issue']
    ]

    for row_data in data:
        sheet.append(row_data)

    # Save the workbook
    file_path = 'Execution_Status_Report.xlsx'
    workbook.save(file_path)
    print(f"Created report: {file_path}")

if __name__ == "__main__":
    # Install openpyxl in your workflow step before running this script
    create_excel_report()

