import json
import hmac
import hashlib
from datetime import datetime, timezone

SIGNING_SECRET = b"hello-there-from-b12"

def main():
    payload = {
        "action_run_link": "ACTION_RUN_LINK_PLACEHOLDER",
        "email": "your-email@example.com",
        "name": "Shrivarshaa Sakhamuri",
        "repository_link": "https://github.com/<your-github-username>/b12-apply",
        "resume_link": "https://www.linkedin.com/in/shrivarshaa-sakhamuri-3a22091a7",
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
