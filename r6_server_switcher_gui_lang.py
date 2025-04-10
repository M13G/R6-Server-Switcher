import os
import tkinter as tk
from tkinter import ttk, messagebox

# Author: Mbg@OxinGame
# Default path to Rainbow Six Siege settings folder
default_path = os.path.expanduser("~/Documents/My Games/Rainbow Six - Siege")

# List of available Rainbow Six Siege data centers
data_centers = [
    "default (ping based)",
    "eastus",
    "centralus",
    "southcentralus",
    "westus",
    "brazilsouth",
    "northeurope",
    "westeurope",
    "southafricanorth",
    "eastasia",
    "southeastasia",
    "australiaeast",
    "australiasoutheast",
    "japanwest",
    "uaenorth"
]

# Language dictionaries
translations = {
    "farsi": {
        "title": "تغییر سرور Rainbow Six Siege",
        "select_server": "یک سرور برای تغییر انتخاب کنید:",
        "apply": "اعمال",
        "note": "توجه: پس از اعمال، بازی را دوباره راه‌اندازی کنید.",
        "author": "نویسنده: Mbg@OxinGame",
        "success_title": "موفقیت",
        "success_msg": "سرور به {} به‌روزرسانی شد\nبرای اعمال تغییرات، بازی را دوباره راه‌اندازی کنید.",
        "error_title": "خطا",
        "error_path": "پوشه تنظیمات Rainbow Six Siege در:\n{} پیدا نشد\nاطمینان حاصل کنید که بازی نصب شده و حداقل یک بار اجرا شده است.",
        "error_file": "فایل GameSettings.ini در پوشه Siege پیدا نشد.\nبازی را یک بار اجرا کنید تا فایل ایجاد شود.",
        "error_update": "خطا در به‌روزرسانی فایل: {}"
    },
    "english": {
        "title": "Rainbow Six Siege Server Switcher",
        "select_server": "Select a server to switch to:",
        "apply": "Apply",
        "note": "Note: Restart the game after applying.",
        "author": "Author: Mbg@OxinGame",
        "success_title": "Success",
        "success_msg": "Server updated to {}\nRestart Rainbow Six Siege to apply changes.",
        "error_title": "Error",
        "error_path": "Could not find the Rainbow Six Siege settings folder at:\n{}\nEnsure the game is installed and has been run at least once.",
        "error_file": "Could not find GameSettings.ini in the Siege folder.\nRun the game once to generate it.",
        "error_update": "Failed to update file: {}"
    }
}

def find_gamesettings_file(base_path):
    """Find the GameSettings.ini file in the Siege directory."""
    for root, dirs, files in os.walk(base_path):
        if "GameSettings.ini" in files:
            return os.path.join(root, "GameSettings.ini")
    return None

def update_settings_file(file_path, new_server):
    """Update the GameSettings.ini file with the new server."""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if "DataCenterHint=" in line:
                if new_server == "default (ping based)":
                    lines[i] = "DataCenterHint=playfab/default\n"
                else:
                    lines[i] = f"DataCenterHint=playfab/{new_server}\n"
                break

        with open(file_path, 'w') as file:
            file.writelines(lines)

        return True
    except Exception as e:
        messagebox.showerror(translations[current_lang]["error_title"], 
                            translations[current_lang]["error_update"].format(str(e)))
        return False

def apply_server_change(server_var, file_path, root):
    """Handle the Apply button click."""
    chosen_server = server_var.get()
    if update_settings_file(file_path, chosen_server):
        messagebox.showinfo(translations[current_lang]["success_title"], 
                           translations[current_lang]["success_msg"].format(chosen_server))
        root.quit()

def update_language(*args):
    """Update GUI text based on selected language."""
    global current_lang
    current_lang = lang_var.get()
    root.title(translations[current_lang]["title"])
    label.config(text=translations[current_lang]["select_server"])
    apply_button.config(text=translations[current_lang]["apply"])
    note_label.config(text=translations[current_lang]["note"])
    author_label.config(text=translations[current_lang]["author"])

def create_gui(file_path):
    """Create the GUI window with language selection."""
    global root, lang_var, label, apply_button, note_label, author_label, current_lang
    root = tk.Tk()
    current_lang = "farsi"  # Default language
    root.geometry("300x200")  # Increased height for language dropdown
    root.resizable(False, False)
    root.configure(bg="#FFFF99")

    style = ttk.Style()
    style.configure("TLabel", background="#FFFF99", foreground="black", font=("Arial", 10))
    style.configure("TButton", background="#FFD700", foreground="black", font=("Arial", 10, "bold"))
    style.map("TButton", background=[("active", "#FFC107")])
    style.configure("TCombobox", fieldbackground="#FFFFFF", background="#FFFF99", foreground="black")

    # Language selection
    lang_var = tk.StringVar(root)
    lang_var.set("farsi")  # Default to Farsi
    lang_dropdown = ttk.Combobox(root, textvariable=lang_var, values=["farsi", "english"], state="readonly")
    lang_dropdown.pack(pady=10)
    lang_var.trace("w", update_language)  # Update GUI when language changes

    # Server selection label
    label = ttk.Label(root, text=translations[current_lang]["select_server"])
    label.pack(pady=5)

    # Server dropdown
    server_var = tk.StringVar(root)
    server_var.set(data_centers[0])
    dropdown = ttk.Combobox(root, textvariable=server_var, values=data_centers, state="readonly")
    dropdown.pack(pady=5)

    # Apply button
    apply_button = ttk.Button(root, text=translations[current_lang]["apply"], 
                             command=lambda: apply_server_change(server_var, file_path, root))
    apply_button.pack(pady=5)

    # Note
    note_label = ttk.Label(root, text=translations[current_lang]["note"], font=("Arial", 8))
    note_label.pack(pady=5)

    # Author credit
    author_label = ttk.Label(root, text=translations[current_lang]["author"], font=("Arial", 8, "italic"))
    author_label.pack(pady=5)

    root.mainloop()

def main():
    if not os.path.exists(default_path):
        messagebox.showerror(translations["farsi"]["error_title"], 
                            translations["farsi"]["error_path"].format(default_path))
        return

    settings_file = find_gamesettings_file(default_path)
    if not settings_file:
        messagebox.showerror(translations["farsi"]["error_title"], 
                            translations["farsi"]["error_file"])
        return

    create_gui(settings_file)

if __name__ == "__main__":
    main()
