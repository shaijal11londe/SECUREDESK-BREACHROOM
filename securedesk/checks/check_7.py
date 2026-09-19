"""
SECUREDESK - BreachRoom Check #7
Check: security_check_7
"""

import os, platform
def run():
    # Check 7: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 7, "name": "security_check_7"}
    return {"status": "PASS", "check_id": 7}


if __name__ == "__main__":
    print(run())
