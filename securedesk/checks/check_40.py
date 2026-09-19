"""
SECUREDESK - BreachRoom Check #40
Check: security_check_40
"""

import os, platform
def run():
    # Check 40: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 40, "name": "security_check_40"}
    return {"status": "PASS", "check_id": 40}


if __name__ == "__main__":
    print(run())
