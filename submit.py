import json
import hmac
import hashlib
import os
from datetime import datetime, timezone

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

    print("JSON body:")
    print(body.decode("utf-8"))
    print()
    print("X-Signature-256:")
    print(f"sha256={signature}")

if __name__ == "__main__":
    main()
