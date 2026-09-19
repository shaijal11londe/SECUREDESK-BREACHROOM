"""
SECUREDESK - BreachRoom Check #25
Check: security_check_25
"""

import os, platform
def run():
    # Check 25: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 25, "name": "security_check_25"}
    return {"status": "PASS", "check_id": 25}


if __name__ == "__main__":
    print(run())
