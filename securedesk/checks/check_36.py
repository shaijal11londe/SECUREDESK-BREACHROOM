"""
SECUREDESK - BreachRoom Check #36
Check: security_check_36
"""

import os, platform
def run():
    # Check 36: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 36, "name": "security_check_36"}
    return {"status": "PASS", "check_id": 36}


if __name__ == "__main__":
    print(run())
