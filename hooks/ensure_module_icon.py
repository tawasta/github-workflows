# hooks/cli_command.py
import os
from pathlib import Path

PASS = 0
FAIL = 1

def main() -> int:
    exit_code = PASS
    """Ensure module icon exists"""
    for d in next(os.walk('.'))[1]:
        # Check if directory is Odoo module directory
        manifest_file = Path(d + "/__manifest__.py")
        if manifest_file.is_file():
            icon_file = Path(d + "/static/description/icon.png")
            if icon_file.is_file():
                pass
            else:
                exit_code = FAIL
                print("Module " + d + " is missing static/description/icon.png")

    return exit_code

if __name__ == "__main__":
    raise SystemExit(main())
