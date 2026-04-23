def assert_status_code(response, expected_status):
    assert response.status_code == expected_status, (
        f"Expected status code {expected_status}, "
        f"but got {response.status_code}"
    )


def assert_json_field_exists(response_json, field):
    assert field in response_json, (
        f"Field '{field}' not present in response"
    )


def assert_json_field_equals(response_json, field, expected_value):
    assert field in response_json, (
        f"Field '{field}' not present in response"
    )
    assert response_json[field] == expected_value, (
        f"Expected '{field}' to be '{expected_value}', "
        f"but got '{response_json[field]}'"
    )
