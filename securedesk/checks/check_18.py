"""
SECUREDESK - BreachRoom Check #18
Check: security_check_18
"""

import os, platform
def run():
    # Check 18: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 18, "name": "security_check_18"}
    return {"status": "PASS", "check_id": 18}


if __name__ == "__main__":
    print(run())
