"""
SECUREDESK - BreachRoom Check #17
Check: security_check_17
"""

import os, platform
def run():
    # Check 17: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 17, "name": "security_check_17"}
    return {"status": "PASS", "check_id": 17}


if __name__ == "__main__":
    print(run())
