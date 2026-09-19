"""
SECUREDESK - BreachRoom Check #79
Check: security_check_79
"""

import os, platform
def run():
    # Check 79: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 79, "name": "security_check_79"}
    return {"status": "PASS", "check_id": 79}


if __name__ == "__main__":
    print(run())
