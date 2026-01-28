import json
import hmac
import hashlib
import os
import urllib.request
from datetime import datetime, timezone

URL = "https://b12.io/apply/submission"
SIGNING_SECRET = b"hello-there-from-b12"

def main():
    repository = os.environ["GITHUB_REPOSITORY"]
    run_id = os.environ["GITHUB_RUN_ID"]

    action_run_link = (
        f"https://github.com/{repository}/actions/runs/{run_id}"
    )

    payload = {
        "action_run_link": action_run_link,
        "email": "shrivarshaasakhamuri@gmail.com",
        "name": "Shrivarshaa Sakhamuri",
        "repository_link":  "https://github.com/ShriVarshaaSakhamuri1/b12-apply",
        "resume_link": "https://www.linkedin.com/in/shrivarshaa-sakhamuri",
        "timestamp": datetime.now(timezone.utc)
            .isoformat(timespec="milliseconds")
            .replace("+00:00", "Z"),
    }

    body = json.dumps(
        payload,
        separators=(",", ":"),
        sort_keys=True,
        ensure_ascii=False,
    ).encode("utf-8")

    signature = hmac.new(
        SIGNING_SECRET,
        body,
        hashlib.sha256
    ).hexdigest()

    headers = {
        "Content-Type": "application/json",
        "X-Signature-256": f"sha256={signature}",
    }

    request = urllib.request.Request(
        URL,
        data=body,
        headers=headers,
        method="POST",
    )

    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
        print(response_body)

if __name__ == "__main__":
    main()
