# hooks/cli_command.py
import os
from pathlib import Path
import hashlib

tawasta_icon_hash = "37df1da0aba9f7e5efabba1b3ddf5021"

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
            if not icon_file.is_file():
                exit_code = FAIL
                print("Module " + d + " is missing static/description/icon.png")
            if hashlib.md5(open(icon_file,'rb').read()).hexdigest() == tawasta_icon_hash:
                exit_code = FAIL
                print("Module " + d + " has old static/description/icon.png")
            else:

    return exit_code

if __name__ == "__main__":
    raise SystemExit(main())
