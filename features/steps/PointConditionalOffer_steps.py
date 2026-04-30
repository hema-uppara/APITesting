import os
from behave import given, when, then
from features.utils.curl_executor import execute_curl_post


@given(u'the Submit PointConditionalOffer API is available')# type: ignore
def step_api_available(context):
    context.url = f"{context.base_url}{context.endpoint}"


@when('I submit a PointConditionalOffer offer using "{payload_file}"')# type: ignore
def step_submit_offer(context, payload_file):
    payload_path = os.path.join("features", "data", payload_file)
    context.response_json, context.status_code = execute_curl_post(
        context.url,
        context.headers,
        payload_path
    )

@then("the PointConditionalOffer response status code should be {expected_status:d}")# type: ignore
def step_validate_status(context, expected_status):
    assert context.status_code == expected_status, (
        f"Expected {expected_status}, got {context.status_code}"
    )


@then("the PointConditionalOffer response should contain {field}")# type: ignore
def step_validate_field(context, field):
    assert field in context.response_json, (
        f"{field} not found in response"
    )


@then('the PointConditionalOffer response status should be "{expected_status}"')# type: ignore
def step_validate_offer_status(context, expected_status):
    assert context.response_json.get("status") == expected_status