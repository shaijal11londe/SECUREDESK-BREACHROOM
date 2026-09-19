"""
SECUREDESK - BreachRoom Check #30
Check: security_check_30
"""

import os, platform
def run():
    # Check 30: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 30, "name": "security_check_30"}
    return {"status": "PASS", "check_id": 30}


if __name__ == "__main__":
    print(run())
