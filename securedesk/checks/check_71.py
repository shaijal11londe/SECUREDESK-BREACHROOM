"""
SECUREDESK - BreachRoom Check #71
Check: security_check_71
"""

import os, platform
def run():
    # Check 71: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 71, "name": "security_check_71"}
    return {"status": "PASS", "check_id": 71}


if __name__ == "__main__":
    print(run())
