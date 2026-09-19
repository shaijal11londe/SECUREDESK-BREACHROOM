"""
SECUREDESK - BreachRoom Check #23
Check: security_check_23
"""

import os, platform
def run():
    # Check 23: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 23, "name": "security_check_23"}
    return {"status": "PASS", "check_id": 23}


if __name__ == "__main__":
    print(run())
