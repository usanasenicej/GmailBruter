# GmailBruterV2 🚀

A powerful and user-friendly Gmail brute-force tool written in Python.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-green.svg)

## 🌟 Features
- **Modern CLI Interface**: Interactive shell with ANSI colors.
- **Cooling Mechanism**: Automatic cooldown to avoid SMTP rate limiting.
- **Config Loading**: Easy loading of session settings from external files.
- **Cross-Platform**: Works on Windows and Linux.
- **Robust Error Handling**: Better management of SMTP connections and file operations.

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/usanasenicej/GmailBruter.git
   cd GmailBruterV2
   ```
2. (Optional) Put your password list in the directory or use the default `PassList.txt`.

## 🚀 Usage
Run the script using Python:
```bash
python GmailBruterV2.py
```

### Commands
- `help`: Show available commands.
- `set target <email>`: Set the target Gmail address.
- `set list <path>`: Set the path to your password list.
- `set time <seconds>`: Set the cooldown duration (default: 60s).
- `show`: View current session configuration.
- `start`: Begin the brute-force attack.
- `load <file>`: Load settings from a configuration file.
- `clear`: Clear the console screen.
- `exit`: Close the program.

### Configuration File Format
You can create a `.txt` file with the following format and load it using the `load` command:
```text
email: target@gmail.com
list: PassList.txt
time: 60
```

## ⚠️ Disclaimer
This tool is for educational purposes and authorized penetration testing only. The author is not responsible for any misuse or damage caused by this program. **Never use this tool to attack accounts you do not own.**

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
