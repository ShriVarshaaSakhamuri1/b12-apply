import json
from datetime import datetime, timezone

def main():
    payload = {
        "action_run_link": "ACTION_RUN_LINK_PLACEHOLDER",
        "email": "shrivarshaasakhamuri@gmail.com",
        "name": "Shrivarshaa Sakhamuri",
        "repository_link": "https://github.com/ShriVarshaaSakhamuri1/b12-apply",
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
    )

    print(body)

if __name__ == "__main__":
    main()
