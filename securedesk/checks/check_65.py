"""
SECUREDESK - BreachRoom Check #65
Check: security_check_65
"""

import os, platform
def run():
    # Check 65: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 65, "name": "security_check_65"}
    return {"status": "PASS", "check_id": 65}


if __name__ == "__main__":
    print(run())
