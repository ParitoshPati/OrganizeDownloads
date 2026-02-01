# OrganizeDownloads

A Python utility that automatically organizes your **Downloads** folder into categorized subfolders. It helps keep your workspace clean, easy to navigate, and auditable with logging.

---

## ✨ Features
- Sorts files by extension into predefined categories:
  - Documents (`.pdf`, `.docx`, `.xlsx`, `.pptx`, `.txt`)
  - Images (`.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`)
  - Videos (`.mp4`, `.mkv`, `.avi`, `.mov`)
  - Audio (`.mp3`, `.wav`, `.aac`)
  - Compressed (`.zip`, `.rar`, `.7z`, `.tar`, `.gz`)
  - Installers (`.exe`, `.msi`)
  - Scripts (`.py`, `.js`, `.sh`, `.bat`)
  - Miscellaneous (anything else)
- Creates folders automatically if they don’t exist.
- Moves uncategorized files into a **Miscellaneous** folder.
- Generates a log file (`organize_log.txt`) with timestamped entries for each run.
- Can be scheduled to run daily using **Windows Task Scheduler**.

---

## 📦 Requirements
- **Windows 11** (tested, should work on other versions too).
- **Python 3.13+** installed on your system.

---

## 🚀 Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/ParitoshPati/OrganizeDownloads.git
   ```
2. Navigate into the project folder:
   ```bash
   cd OrganizeDownloads
   ```
3. Ensure Python is installed:
   ```bash
   python --version
   ```
   or
   ```bash
   py --version
   ```

---

## ▶️ Usage
Run the script manually:
```bash
python organize_downloads.py
```

This will:
- Scan your Downloads folder.
- Move files into categorized subfolders.
- Append a log entry in `organize_log.txt`.

---

## ⚡ Automating with Task Scheduler
1. Open **Task Scheduler** on Windows.
2. Click **Create Basic Task** → name it *Organize Downloads*.
3. Set a trigger (e.g., **Daily at 8:00 PM**).
4. In **Action → Start a Program**:
   - **Program/script**: full path to `python.exe`  
     Example:  
     `C:\Users\Lenovo\AppData\Local\Programs\Python\Python313\python.exe`
   - **Add arguments**: full path to your script  
     Example:  
     `"C:\Users\Lenovo\OneDrive\Desktop\organize_downloads.py"`
   - **Start in**: folder containing your script  
     Example:  
     `C:\Users\Lenovo\OneDrive\Desktop`
5. Finish setup and test by running the task manually.

---

## 📝 Log File
Each run appends entries to `organize_log.txt` in your Downloads folder:
```
--- Run at 2026-02-01 09:56:00 ---
Moved example.pdf → Documents
Moved photo.png → Images
Moved setup.exe → Installers
```

---

## 🔧 Customization
- Add or remove file extensions in the `categories` dictionary.
- Change the log file location by editing the `log_file` path.
- Add cleanup rules (e.g., delete installers older than 30 days).
- Extend categories (e.g., `Ebooks`, `Spreadsheets`, `Design Assets`).

---

## 🛠 Troubleshooting
- **Error 0x80070002 in Task Scheduler**:  
  This means Windows cannot find the file. Double‑check:
  - Full path to `python.exe` in **Program/script**.
  - Full path to your `.py` file in **Add arguments**.
  - Correct folder in **Start in**.
  - Use quotes around paths with spaces.

- **Python not found**:  
  Locate `python.exe` manually in:
  ```
  C:\Users\<YourName>\AppData\Local\Programs\Python\Python3xx\
  ```
  Then update Task Scheduler with the correct path.

---

## 📄 License
This project is licensed under the MIT License. Feel free to use and modify it.

---

## 👤 Author
Developed by Paritosh [(github.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fgithub.com%2FParitoshPati").
```

---


