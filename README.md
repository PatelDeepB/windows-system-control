# 🖥️ pyRD - Python Remote Desktop Control Tool

**pyRD** is a Python-based remote desktop utility that allows you to monitor and control a Windows system remotely. It integrates Flask for web-based control, and includes various supporting modules and scripts to enable smooth desktop interaction.

---

## 📁 Project Structure

```
pyRD/
├── build/                  # PyInstaller build files
├── dist/                   # Final executable files
├── templates/              # Flask HTML templates
├── app.py                  # Main Flask app
├── myremote.py             # Remote desktop logic handler
├── remote.py               # Remote control implementation
├── remote2.py              # Extended remote features
├── remote3.py              # Additional control logic
├── size.py                 # Screen size or resolution utilities
├── pyRD.png                # App icon
├── screen.bmp              # Screenshot or splash
├── ss.png                  # GUI snapshot
├── myremote.spec           # PyInstaller spec file
├── LICENSE                 # Project license (MIT or custom)
├── README.md               # This file
```

---

## ✨ Features

- 🖥️ Web-based interface to control your system remotely
- 🎯 Real-time screen capture and interaction
- 🧠 Modular design with `remote.py`, `remote2.py`, `remote3.py` for extendable features
- 📦 Easily converted to executable using PyInstaller
- 🪟 Built for Windows systems (other OS not tested)

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/pyRD.git
cd pyRD
```

### 2. (Optional) Create and activate a virtual environment

```bash
python -m venv venv
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
# Or install manually if requirements.txt not available
```

### 4. Run the app

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser to use the web interface.

---

## 🛠️ Build Executable (Optional)

To create a standalone Windows `.exe`:

```bash
pyinstaller myremote.spec
```

The built executable will be located in the `dist/` directory.

---

## 📸 Screenshots

Here are some visuals of the application in action:

- `pyRD.png` - App icon
- `screen.bmp` - Screenshot / splash
- `ss.png` - Web interface or GUI preview

*(Add these images directly in your GitHub repo and link them here if needed)*

---

## 📄 License

This project is licensed under the terms of the [LICENSE](./LICENSE) file.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change or improve.

---

## 🔗 Author

Built with ❤️ by [Your Name]  
📧 Contact: your.email@example.com  
🌐 GitHub: [yourusername](https://github.com/yourusername)

---

> ⚠️ **Disclaimer:** This tool is intended for educational and personal use only. Use responsibly and with appropriate permissions on target systems.
