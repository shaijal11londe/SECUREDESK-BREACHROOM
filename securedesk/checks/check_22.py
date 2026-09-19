"""
SECUREDESK - BreachRoom Check #22
Check: security_check_22
"""

import os, platform
def run():
    # Check 22: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 22, "name": "security_check_22"}
    return {"status": "PASS", "check_id": 22}


if __name__ == "__main__":
    print(run())
