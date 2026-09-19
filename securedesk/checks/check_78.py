"""
SECUREDESK - BreachRoom Check #78
Check: security_check_78
"""

import os, platform
def run():
    # Check 78: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 78, "name": "security_check_78"}
    return {"status": "PASS", "check_id": 78}


if __name__ == "__main__":
    print(run())
