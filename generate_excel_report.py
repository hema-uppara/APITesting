import pandas as pd
import xml.etree.ElementTree as ET
import sys

def parse_xml_to_excel(xml_file, excel_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    test_results = []
    for testsuite in root.findall('testsuite'):
        for testcase in testsuite.findall('testcase'):
            test_name = testcase.get('name')
            class_name = testcase.get('classname')
            duration = testcase.get('time')
            status = 'Passed'
            if testcase.find('failure') is not None:
                status = 'Failed'
            elif testcase.find('skipped') is not None:
                status = 'Skipped'
            
            test_results.append({
                'Test Case': f"{class_name}.{test_name}",
                'Status': status,
                'Duration (s)': duration
            })

    df = pd.DataFrame(test_results)
    # Use Pandas ExcelWriter with openpyxl engine to save as .xlsx
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Test Results')
    print(f"Generated Excel report: {excel_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_excel_report.py <input_xml_file> <output_excel_file>")
        sys.exit(1)
    input_xml = sys.argv[1]
    output_excel = sys.argv[2]
    parse_xml_to_excel(input_xml, output_excel)

