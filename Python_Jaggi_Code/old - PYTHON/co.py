import os
import shutil

# Set the directory you want to organize
TARGET_DIR = r"D:\\"  # Change if needed

FILE_GROUPS = {
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Video": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".rtf", ".xlsx", ".pptx"],
    "Python_Files": [".py"],
    "Java_Files": [".java"],
    "C_CPP_Files": [".c", ".cpp", ".h", ".hpp"]
}

def organize_files(base_path):
    for root, dirs, files in os.walk(base_path):
        # Skip newly created folders to avoid infinite loops
        if os.path.basename(root) in FILE_GROUPS.keys():
            continue

        for file in files:
            file_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()

            for folder, extensions in FILE_GROUPS.items():
                if ext in extensions:
                    dest_folder = os.path.join(base_path, folder)
                    os.makedirs(dest_folder, exist_ok=True)

                    try:
                        shutil.move(file_path, os.path.join(dest_folder, file))
                        print(f"Moved: {file} -> {folder}")
                    except Exception as e:
                        print(f"Error moving {file}: {e}")
                    break

if __name__ == "__main__":
    organize_files(TARGET_DIR)
    print("File organization completed.")
