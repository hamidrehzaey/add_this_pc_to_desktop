import os, winsound, time
import winreg as reg

# Registry key path for showing desktop icons
desktop_icon_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\HideDesktopIcons\NewStartPanel"

# Opening the registry key and setting the value to show "This PC"
try:
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, desktop_icon_path, 0, reg.KEY_SET_VALUE)
    # Change the value related to "This PC" to 0 to enable it
    reg.SetValueEx(key, "{20D04FE0-3AEA-1069-A2D8-08002B30309D}", 0, reg.REG_DWORD, 0)
    reg.CloseKey(key)
    winsound.Beep(1000, 500)
except Exception as e:
    print("Error in setting the registry:", e)

# Restarting Windows Explorer
time.sleep(1)  # Short delay
os.system("taskkill /f /im explorer.exe")
time.sleep(1)
os.system("start explorer.exe")
winsound.Beep(1000, 500)
