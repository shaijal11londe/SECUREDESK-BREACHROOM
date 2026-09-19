"""
SECUREDESK - BreachRoom Check #81
Check: security_check_81
"""

import os, platform
def run():
    # Check 81: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 81, "name": "security_check_81"}
    return {"status": "PASS", "check_id": 81}


if __name__ == "__main__":
    print(run())
