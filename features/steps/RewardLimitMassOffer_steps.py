import os
from behave import given, when, then
from features.utils.curl_executor import execute_curl_post


@given("the Submit RewardLimitMassOffer Offer API is available")
def step_api_available(context):
    context.url = f"{context.base_url}{context.endpoint}"


@when('I submit a RewardLimitMassOffer offer using "{payload_file}"')
def step_submit_offer(context, payload_file):
    payload_path = os.path.join("features", "data", payload_file)
    context.response_json, context.status_code = execute_curl_post(
        context.url,
        context.headers,
        payload_path
    )

@then("the RewardLimitMassOffer response status code should be {expected_status:d}")
def step_validate_status(context, expected_status):
    assert context.status_code == expected_status, (
        f"Expected {expected_status}, got {context.status_code}"
    )


@then("the RewardLimitMassOffer response should contain {field}")
def step_validate_field(context, field):
    assert field in context.response_json, (
        f"{field} not found in response"
    )


@then('the RewardLimitMassOffer response status should be "{expected_status}"')
def step_validate_offer_status(context, expected_status):
    assert context.response_json.get("status") == expected_status