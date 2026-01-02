import os
import shutil
import sys
import time


# ---------------------------------------------------
# Show Usage (--u / --U)
# ---------------------------------------------------
def show_usage():
    print("""
-----------------------------------------
Usage Guide (How to use this script)
-----------------------------------------

1) Run normally (no deletion):
   python auto_organizer.py

   - Organizes files by extension
   - Keeps empty files
   - Keeps empty folders

2) Run with deletion mode:
   python auto_organizer.py del

   - Organizes files by extension
   - Deletes empty files
   - Deletes empty folders

3) View usage help:
   python auto_organizer.py --u
   python auto_organizer.py --U

4) View what this script does:
   python auto_organizer.py --h
   python auto_organizer.py --H
-----------------------------------------
""")


# ---------------------------------------------------
# Show Description (--h / --H)
# ---------------------------------------------------
def show_help():
    print("""
-----------------------------------------
What this script does
-----------------------------------------
This script automatically arranges files inside
the current working directory and its sub-folders.

Features:
- Organizes files into folders based on extension
- Removes empty files (only in `del` mode)
- Removes empty directories (only in `del` mode`)
- Runs every 1 minute automatically
- No GUI - fully command-line based
-----------------------------------------
""")


# ---------------------------------------------------
# Delete empty files
# ---------------------------------------------------
def delete_empty_files(path):
    removed_files = 0

    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            if os.path.isfile(full_path) and os.path.getsize(full_path) == 0:
                os.remove(full_path)
                removed_files += 1

    return removed_files


# ---------------------------------------------------
# Delete empty directories
# ---------------------------------------------------
def delete_empty_folders(path):
    removed_dirs = 0

    for root, dirs, files in os.walk(path, topdown=False):
        if not os.listdir(root):  # folder empty
            os.rmdir(root)
            removed_dirs += 1

    return removed_dirs


# ---------------------------------------------------
# Main file arranging logic
# ---------------------------------------------------
def arrange_files(path):
    arranged_count = 0

    for root, dirs, files in os.walk(path):
        for filename in files:
            src_path = os.path.join(root, filename)

            # skip arranged folders
            if os.path.basename(root).startswith("arranged_"):
                continue

            extension = filename.split(".")[-1].lower() if "." in filename else "no_extension"
            target_folder = os.path.join(path, f"arranged_{extension}")

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            try:
                shutil.move(src_path, os.path.join(target_folder, filename))
                arranged_count += 1
            except:
                pass

    return arranged_count


# ---------------------------------------------------
# MAIN SCRIPT (Auto-run every 1 minute)
# ---------------------------------------------------
def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()

        if arg in ["--u", "--U"]:
            show_usage()
            return

        if arg in ["--h", "--H"]:
            show_help()
            return

        delete_mode = (arg == "del")
    else:
        delete_mode = False

    folder_path = os.getcwd()

    print("\nAutomation Started (Press CTRL + C to stop)")
    print(f"Monitoring Folder: {folder_path}")
    print("Arranging every 1 minute...\n")

    try:
        while True:
            arranged = arrange_files(folder_path)

            if delete_mode:
                empty_removed = delete_empty_files(folder_path)
                folder_removed = delete_empty_folders(folder_path)
                print(f"Arranged: {arranged} | Deleted empty files: {empty_removed} | Deleted empty folders: {folder_removed}")
            else:
                print(f"Arranged: {arranged} | Empty files/folders kept")

            print("Waiting 1 minute...\n")
            time.sleep(60)

    except KeyboardInterrupt:
        print("\nAutomation stopped by user.")


if __name__ == "__main__":
    main()
