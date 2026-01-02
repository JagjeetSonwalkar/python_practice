import os
import shutil

# Folder to scan
TARGET_DIR = r"D:\\"

# Extension groups
EXT_GROUPS = {
    "Python_Files": [".py"],
    "Java_Files": [".java"],
    "Class_Files": [".class"],
    "C_Files": [".c"],
    "CPP_Files": [".cpp"],
    "Text_Files": [".txt"],

    "Audio_Files": [
        ".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"
    ],

    "Video_Files": [
        ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".mpeg", ".mpg"
    ],

    # Document formats (NEW)
    "Document_Files": [
        ".pdf", ".doc", ".docx", ".ppt", ".pptx",
        ".xls", ".xlsx", ".odt", ".ods"
    ]
}

# Flatten extension → folder mapping
EXT_TO_FOLDER = {}
for folder, extensions in EXT_GROUPS.items():
    for ext in extensions:
        EXT_TO_FOLDER[ext] = folder


def organize_files(base_path):
    for root, dirs, files in os.walk(base_path):

        # Skip our destination folders (prevent infinite loop)
        if os.path.basename(root) in EXT_GROUPS.keys():
            continue

        for file in files:
            ext = os.path.splitext(file)[1].lower()

            if ext in EXT_TO_FOLDER:
                src = os.path.join(root, file)
                dest_folder = os.path.join(base_path, EXT_TO_FOLDER[ext])

                os.makedirs(dest_folder, exist_ok=True)

                try:
                    shutil.move(src, os.path.join(dest_folder, file))
                    print(f"Moved: {src} --> {dest_folder}")
                except Exception as e:
                    print(f"Error moving {file}: {e}")


if __name__ == "__main__":
    organize_files(TARGET_DIR)
    print("Completed: All files organized successfully.")
