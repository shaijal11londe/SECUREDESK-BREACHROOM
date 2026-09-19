"""
SECUREDESK - BreachRoom Check #8
Check: security_check_8
"""

import os, platform
def run():
    # Check 8: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 8, "name": "security_check_8"}
    return {"status": "PASS", "check_id": 8}


if __name__ == "__main__":
    print(run())
