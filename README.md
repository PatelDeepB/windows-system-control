# 🖥️ Sample Flask-Tkinter App for Windows System Control

This project is a simple yet powerful hybrid application built using **Flask** and **Tkinter**. It allows you to **control and monitor your Windows system** through a web-based interface served via Flask and a native GUI using Tkinter.

---

## 📁 Project Structure

```
sample-flask-tkinter-app/
├── build/
├── dist/
├── static/
│   └── ...        # Static web assets
├── index.html     # Main HTML page served by Flask
├── screen.py      # Core Python script for GUI and backend logic
├── screen.spec    # PyInstaller spec file
├── requirements.txt
```

---

## ✨ Features

- View Windows system status from a web interface.
- Native Tkinter GUI window for local control.
- Flask server backend to handle real-time updates.
- Designed to be converted into a standalone executable using PyInstaller.

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/sample-flask-tkinter-app.git
cd sample-flask-tkinter-app
```

### 2. Create a virtual environment (optional but recommended)

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
```

### 4. Run the application

```bash
python screen.py
```

---

## 🛠️ Convert to Executable (Optional)

Use **PyInstaller** to package the application as a Windows executable:

```bash
pyinstaller screen.spec
```

The final executable will be located in the `dist/` directory.

---

## 📷 Screenshots

*(Add screenshots of your Flask interface or Tkinter app here for better presentation)*

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for more details.

---

## 🙌 Contributions

Feel free to open issues or submit pull requests to improve the project. Suggestions and feedback are welcome!

---

## 🔗 Author

Built with ❤️ by [Deep Patel]  
📧 Contact: deepbpatel9898@gmail.com  
🌐 GitHub: [PatelDeepB](https://github.com/PatelDeepB)
