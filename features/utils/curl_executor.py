import subprocess
import json
import os


def execute_curl_post(url, headers, payload_path):
    payload_path = os.path.abspath(payload_path)

    if not os.path.exists(payload_path):
        raise Exception(f"Payload file not found: {payload_path}")

    curl_cmd = [
        "curl",
        "--location",
        "--silent",
        "--show-error",
        "-X", "POST",
        url
    ]

    for key, value in headers.items():
        curl_cmd.extend(["-H", f"{key}: {value}"])

    curl_cmd.extend([
        "--data", f"@{payload_path}",
        "--write-out", "\nHTTP_STATUS:%{http_code}"
    ])

    result = subprocess.run(
        curl_cmd,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise Exception(f"CURL failed:\n{result.stderr}")

    # ✅ Split body and status code safely
    try:
        response_body, status_line = result.stdout.rsplit("\nHTTP_STATUS:", 1)
        status_code = int(status_line.strip())
    except ValueError:
        raise Exception(f"Failed to parse CURL output:\n{result.stdout}")

    # ✅ Parse JSON body
    try:
        response_json = json.loads(response_body.strip())
    except json.JSONDecodeError as e:
        raise Exception(f"Invalid JSON response:\n{response_body}") from e

    return response_json, status_code