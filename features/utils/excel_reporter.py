import pandas as pd
from datetime import datetime
import os

_RESULTS = []


def log_result(feature, scenario, status, tags):
    _RESULTS.append({
        "Feature": feature,
        "Test Case Name": scenario,
        "Status": status,
        "Tags": ", ".join(tags)
    })


def write_excel_report():
    if not _RESULTS:
        return

    df = pd.DataFrame(_RESULTS)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("reports", exist_ok=True)

    file_path = f"reports/ESTAF_Behave_Execution_Report_{timestamp}.xlsx"
    df.to_excel(file_path, index=False)

    print(f"\n✅ Excel report generated: {file_path}")
    
    