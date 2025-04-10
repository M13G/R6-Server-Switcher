# Rainbow Six Siege Server Switcher

A simple GUI application to manually switch Rainbow Six Siege servers by modifying the `GameSettings.ini` file. Built with Python and `tkinter`, this tool supports both English and Farsi languages and features a customizable yellow theme.

**Author**: Mbg 
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
- **Author Credit**: Displays "Author: Mbg@OxinGame" (or "نویسنده: Mbg@OxinGame" in Farsi) in the GUI.

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
   ```
   Replace `[YourUsername]` and `[YourRepoName]` with your GitHub username and repository name.

2. **Run the Script**:
   ```bash
   python r6_server_switcher_gui_lang.py
   ```
   This launches the app directly from the source code.

---

## Usage

1. **Launch the App**:
   - Run the `.py` file with Python or double-click the `.exe` (if built).
2. **Select Language**:
   - Use the top dropdown to choose "English" or "Farsi" (defaults to Farsi).
3. **Choose a Server**:
   - Use the second dropdown to select a data center (e.g., `uaenorth`, `default (ping based)`).
4. **Apply Changes**:
   - Click "Apply" (or "اعمال" in Farsi) to update the `GameSettings.ini` file.
   - A success message will confirm the change (e.g., "Server updated to uaenorth").
5. **Restart the Game**:
   - Close and relaunch Rainbow Six Siege to apply the new server setting.

### Notes
- The app looks for `GameSettings.ini` in `~/Documents/My Games/Rainbow Six - Siege/`. Ensure the game has been run at least once to generate this file.
- If the file or folder isn’t found, an error message will appear in the selected language.

---

## Building the Executable

To create a standalone `.exe` for Windows:

1. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

2. **Build the `.exe`**:
   - Basic command:
     ```bash
     pyinstaller --onefile --windowed r6_server_switcher_gui_lang.py
     ```
   - With a custom icon (e.g., `r6_switcher_icon.ico`):
     ```bash
     pyinstaller --onefile --windowed --icon=r6_switcher_icon.ico r6_server_switcher_gui_lang.py
     ```
   - The `.exe` will be in the `dist` folder.

3. **Custom Icon** (Optional):
   - Design an icon (e.g., 256x256 PNG) with a light yellow background (`#FFFF99`), a black "6," vertical Farsi "سرور," and a `#FFD700` ring.
   - Convert to `.ico` using [icoconvert.com](https://icoconvert.com/) with sizes 16x16, 32x32, 64x64, 128x128, 256x256.
   - Place the `.ico` file in the same directory as the script before running PyInstaller.

---

## Contributing

Contributions are welcome! To contribute:

1. **Fork the Repository**:
   - Click "Fork" on the GitHub page.
2. **Make Changes**:
   - Clone your fork, edit the code, and test locally.
3. **Submit a Pull Request**:
   - Push your changes to your fork and create a pull request to the main repository.

### Ideas for Improvement
- Add more data centers as Ubisoft updates them.
- Support additional languages (e.g., Arabic, Spanish).
- Enhance the GUI with custom fonts or themes.
- Add error logging to a file for debugging.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Mbg@OxinGame

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

---

---
