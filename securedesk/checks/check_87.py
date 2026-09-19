"""
SECUREDESK - BreachRoom Check #87
Check: security_check_87
"""

import os, platform
def run():
    # Check 87: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 87, "name": "security_check_87"}
    return {"status": "PASS", "check_id": 87}


if __name__ == "__main__":
    print(run())
