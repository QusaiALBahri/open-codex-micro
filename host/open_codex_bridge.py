"""Optional serial bridge for custom desktop integrations.

The reference firmware works without this file. A future firmware profile may
send newline-delimited events such as ``key:approve`` or ``encoder:right``.
This utility prints them in a stable format so a user can pipe them into a
local script, window manager, or accessibility tool without a cloud service.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Read Open Codex Micro serial events")
    parser.add_argument("port", help="Serial port, for example COM7 or /dev/ttyACM0")
    parser.add_argument("--baud", type=int, default=115200)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        import serial
    except ImportError:
        print("Install the optional host dependency with: python -m pip install pyserial", file=sys.stderr)
        return 2

    port = Path(args.port)
    with serial.Serial(str(port), args.baud, timeout=1) as connection:
        print(f"Listening on {port}. Press Ctrl+C to stop.")
        try:
            while True:
                line = connection.readline().decode("utf-8", errors="replace").strip()
                if line:
                    print(line, flush=True)
        except KeyboardInterrupt:
            return 0


if __name__ == "__main__":
    raise SystemExit(main())


