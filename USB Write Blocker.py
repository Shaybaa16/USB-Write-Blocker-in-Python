import tkinter as tk
from tkinter import messagebox
import ctypes
import winreg

# Function to enable write protection
def enable_write_protection():
    try:
        registry_path = r"SYSTEM\CurrentControlSet\Control\StorageDevicePolicies"
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "WriteProtect", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
        messagebox.showinfo("Success", "Write protection enabled for USB devices.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to enable write protection: {e}")

# Function to disable write protection
def disable_write_protection():
    try:
        registry_path = r"SYSTEM\CurrentControlSet\Control\StorageDevicePolicies"
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "WriteProtect", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        messagebox.showinfo("Success", "Write protection disabled for USB devices.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to disable write protection: {e}")

# Check if the script is running with admin privileges
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Main function to build GUI
def main():
    if not is_admin():
        messagebox.showerror("Error", "Please run the script as an administrator.")
        return
    
    # Create the main window
    root = tk.Tk()
    root.title("USB Write Blocker")
    root.geometry("400x200")
    root.resizable(False, False)

    # Add a label for the title
    title_label = tk.Label(root, text="USB Write Blocker", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    # Add a description label
    desc_label = tk.Label(root, text="Select an option to enable or disable write protection\non external USB storage devices.", font=("Arial", 10))
    desc_label.pack(pady=5)

    # Add buttons for enabling/disabling write protection
    enable_button = tk.Button(root, text="Enable Write Protection", font=("Arial", 12), bg="#4CAF50", fg="white", command=enable_write_protection)
    enable_button.pack(pady=10, ipadx=20)

    disable_button = tk.Button(root, text="Disable Write Protection", font=("Arial", 12), bg="#F44336", fg="white", command=disable_write_protection)
    disable_button.pack(pady=10, ipadx=20)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
