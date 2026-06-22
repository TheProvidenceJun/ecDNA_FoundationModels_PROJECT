import platform
import sys
from datetime import datetime, timezone


def main():
    utc_now = datetime.now(timezone.utc).replace(microsecond=0)
    lines = [
        "harness smoke test OK",
        f"python: {sys.version.split()[0]}",
        f"utc: {utc_now.isoformat().replace('+00:00', 'Z')}",
        f"platform: {platform.platform()}",
    ]
    text = "\n".join(lines) + "\n"

    print(text, end="")
    with open("outputs/smoke_test_result.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
