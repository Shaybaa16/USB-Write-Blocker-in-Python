**USB Write Protection Utility**

This Python application provides a simple GUI interface to enable or disable write protection on USB storage devices. It modifies the Windows registry to control the write protection setting.

**Key Features:**
Enable Write Protection: 
Prevents data from being written to USB devices.

Disable Write Protection:
Allows data to be written to USB devices again.

User-Friendly Interface: 
Built using tkinter for easy interaction.

Error Handling: 
Displays success or error messages to inform the user of the operation status.

Technical Details:
Registry Path Modified: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\StorageDevicePolicies

WriteProtect Key:
1 for enabling write protection.
0 for disabling write protection.

**Requirements:**
Python 3.x
tkinter library (usually included with Python installations)
Administrative privileges to modify the registry.
