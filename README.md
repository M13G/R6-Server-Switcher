# Rainbow Six Siege Server Switcher

A simple GUI application to manually switch Rainbow Six Siege servers by modifying the `GameSettings.ini` file. Built with Python and `tkinter`, this tool supports both English and Farsi languages and features a customizable yellow theme.

**Author**: MbG  
**GitHub**: github.com/M13G  
**License**: MIT License

---

## Overview

This application allows Rainbow Six Siege players to easily change their server (data center) by selecting from a list of available options. It automates the process of editing the `DataCenterHint` value in the game's configuration file, supporting regions like `uaenorth` (UAE North) and more. The app offers a bilingual interface (English and Farsi) and a visually appealing yellow-themed GUI.

---

## Features

- **Server Selection**: Choose from a list of Rainbow Six Siege data centers, including `default (ping based)`, `eastus`, `westeurope`, `uaenorth`, and more.
- **Bilingual Support**: Switch between English and Farsi languages dynamically via a dropdown menu.
- **User-Friendly GUI**: Built with `tkinter`, featuring a light yellow background (`#FFFF99`) and a darker yellow button (`#FFD700`).
- **Cross-Platform**: Runs on Windows (and potentially other OSes with Python installed).
- **Portable Executable**: Can be compiled into a standalone `.exe` using PyInstaller.
- **Author Credit**: Displays "Author: MbG" (or "نویسنده: MbG" in Farsi) in the GUI.

---

## Installation

### Prerequisites
- **Python**: Version 3.6 or higher (download from [python.org](https://www.python.org/)).
- **tkinter**: Included with standard Python installations.
- **PyInstaller** (optional): For building the `.exe` (install via `pip install pyinstaller`).

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/[YourUsername]/[YourRepoName].git
   cd [YourRepoName]
