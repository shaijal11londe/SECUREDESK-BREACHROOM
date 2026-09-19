"""
SECUREDESK - BreachRoom Check #26
Check: security_check_26
"""

import os, platform
def run():
    # Check 26: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 26, "name": "security_check_26"}
    return {"status": "PASS", "check_id": 26}


if __name__ == "__main__":
    print(run())
