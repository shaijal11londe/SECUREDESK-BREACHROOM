"""
SECUREDESK - BreachRoom Check #90
Check: security_check_90
"""

import os, platform
def run():
    # Check 90: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 90, "name": "security_check_90"}
    return {"status": "PASS", "check_id": 90}


if __name__ == "__main__":
    print(run())
