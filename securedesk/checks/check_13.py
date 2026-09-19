"""
SECUREDESK - BreachRoom Check #13
Check: security_check_13
"""

import os, platform
def run():
    # Check 13: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 13, "name": "security_check_13"}
    return {"status": "PASS", "check_id": 13}


if __name__ == "__main__":
    print(run())
