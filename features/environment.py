

from datetime import datetime
from features.utils.excel_reporter import log_result, write_excel_report



def before_all(context):

    context.base_url = "https://ms-api-gateway-qa.azurewebsites.net"
    context.endpoint = "/offers/v1/offers/submit"

    context.headers = {
        "countryCode": "GB",
        "Content-Type": "application/json"
    }

def before_scenario(context, scenario):
    scenario.start_time = datetime.now()

def after_scenario(context, scenario):
    duration = (datetime.now() - scenario.start_time).total_seconds()
    status = "Passed" if scenario.status == "passed" else "Failed"
    log_result(
        feature=scenario.feature.name,
        scenario=scenario.name,
        status=status,
        tags=scenario.effective_tags,
    )


def after_all(context):
    write_excel_report()
