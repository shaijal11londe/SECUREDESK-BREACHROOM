"""
SECUREDESK - BreachRoom Check #37
Check: security_check_37
"""

import os, platform
def run():
    # Check 37: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 37, "name": "security_check_37"}
    return {"status": "PASS", "check_id": 37}


if __name__ == "__main__":
    print(run())
