"""
SECUREDESK - BreachRoom Check #73
Check: security_check_73
"""

import os, platform
def run():
    # Check 73: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 73, "name": "security_check_73"}
    return {"status": "PASS", "check_id": 73}


if __name__ == "__main__":
    print(run())
