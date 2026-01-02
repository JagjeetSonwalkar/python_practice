import os
import shutil

def collect_py_files(root):

    target = os.path.join(root, "python_files")

    # create folder if not exists
    if not os.path.exists(target):
        os.makedirs(target)

    moved = 0

    # walk through all subdirectories
    for current_root, dirs, files in os.walk(root):
        for file in files:

            # only .py files
            if file.lower().endswith(".py"):
                src = os.path.join(current_root, file)
                dst = os.path.join(target, file)

                # if same name exists, rename to avoid overwrite
                if os.path.exists(dst):
                    name, ext = os.path.splitext(file)
                    dst = os.path.join(target, f"{name}_copy{ext}")

                try:
                    shutil.move(src, dst)
                    moved += 1
                except Exception as e:
                    print("Could not move:", src, "| Error:", e)

    print(f"Total .py files moved: {moved}")
    print(f"All Python files stored in: {target}")


if __name__ == "__main__":
    root_folder = os.getcwd()
    collect_py_files(root_folder)
