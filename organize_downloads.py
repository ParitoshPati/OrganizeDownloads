import os
import shutil
from datetime import datetime

# Path to your Downloads folder
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

# Path to log file
log_file = os.path.join(downloads_path, "organize_log.txt")

# Define categories and file extensions
categories = {
    "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".pptx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Compressed": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Installers": [".exe", ".msi"],
    "Scripts": [".py", ".js", ".sh", ".bat"]
}

# Create folders if they don't exist
for folder in categories.keys():
    folder_path = os.path.join(downloads_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Create Miscellaneous folder if needed
misc_path = os.path.join(downloads_path, "Miscellaneous")
if not os.path.exists(misc_path):
    os.makedirs(misc_path)

# Open log file
with open(log_file, "a", encoding="utf-8") as log:
    log.write(f"\n--- Run at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")

    # Move files into categorized folders
    for file in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, file)
        if os.path.isfile(file_path) and file != "organize_log.txt":
            _, ext = os.path.splitext(file)
            moved = False
            for category, extensions in categories.items():
                if ext.lower() in extensions:
                    shutil.move(file_path, os.path.join(downloads_path, category, file))
                    log.write(f"Moved {file} → {category}\n")
                    moved = True
                    break
            if not moved:
                shutil.move(file_path, os.path.join(misc_path, file))
                log.write(f"Moved {file} → Miscellaneous\n")

print("Downloads folder organized successfully! Log updated.")