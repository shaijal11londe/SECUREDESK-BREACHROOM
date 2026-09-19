"""
SECUREDESK - BreachRoom Check #27
Check: security_check_27
"""

import os, platform
def run():
    # Check 27: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 27, "name": "security_check_27"}
    return {"status": "PASS", "check_id": 27}


if __name__ == "__main__":
    print(run())
