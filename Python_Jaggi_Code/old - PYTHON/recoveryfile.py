import os
import shutil

def restore(root):
    for item in os.listdir(root):
        folder = os.path.join(root, item)

        # only restore from arranged_ folders
        if os.path.isdir(folder) and item.startswith("arranged_"):
            for filename in os.listdir(folder):
                src = os.path.join(folder, filename)
                dst = os.path.join(root, filename)

                try:
                    if os.path.exists(dst):
                        # avoid overwriting
                        base, ext = os.path.splitext(filename)
                        dst = os.path.join(root, f"{base}_restored{ext}")

                    shutil.move(src, dst)
                except Exception as e:
                    print(f"Cannot move: {src} -> {dst}", e)

            # remove empty arranged folder
            try:
                os.rmdir(folder)
            except:
                pass

    print("Restore complete.")

if __name__ == "__main__":
    restore(os.getcwd())
