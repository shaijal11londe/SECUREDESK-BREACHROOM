"""
SECUREDESK - BreachRoom Check #2
Check: usb_storage_blocked
"""

import winreg
def run():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\USBSTOR")
        val = winreg.QueryValueEx(key, "Start")[0]
        if val == 4: return {"status": "PASS", "msg": "USB Blocked"}
        return {"status": "FAIL", "msg": "USB Not Blocked"}
    except:
        return {"status": "FAIL", "msg": "Cannot read registry"}


if __name__ == "__main__":
    print(run())
