import os

HEADER_SIZE = 300   # enough space for filename + filesize

def pack_files():
    print("Enter the name of directory to pack:")
    dir_name = input().strip()

    print("Enter the name of packed file to create:")
    pack_name = input().strip()

    if not os.path.isdir(dir_name):
        print("Invalid directory.")
        return

    file_list = [f for f in os.listdir(dir_name)
                 if os.path.isfile(os.path.join(dir_name, f))]

    if not file_list:
        print("No files found in the directory.")
        return

    try:
        with open(pack_name, "wb") as pack_file:
            total_packed = 0
            buffer_size = 4096  # safe for large media files

            for file_name in file_list:
                file_path = os.path.join(dir_name, file_name)
                file_size = os.path.getsize(file_path)

                # Create header: "filename filesize"
                header = f"{file_name} {file_size}"
                header = header.ljust(HEADER_SIZE)

                pack_file.write(header.encode("utf-8"))

                # Write file data
                with open(file_path, "rb") as f:
                    while True:
                        data = f.read(buffer_size)
                        if not data:
                            break
                        pack_file.write(data)

                total_packed += 1

        print(f"Total files packed: {total_packed}")

    except Exception as e:
        print(f"Packing error: {e}")


def unpack_files():
    print("Enter the packed file to unpack:")
    pack_name = input().strip()

    if not os.path.exists(pack_name):
        print("Packed file does not exist.")
        return

    try:
        with open(pack_name, "rb") as pack_file:
            buffer_size = 4096
            total_unpacked = 0

            while True:
                header_data = pack_file.read(HEADER_SIZE)

                if not header_data:
                    break  # end of packed file

                header = header_data.decode("utf-8").strip()

                # parse header: filename filesize
                parts = header.split(" ")
                filename = parts[0]
                filesize = int(parts[-1])

                output_name = f"unpacked_{filename}"

                with open(output_name, "wb") as out_file:
                    remaining = filesize

                    while remaining > 0:
                        chunk = pack_file.read(min(buffer_size, remaining))
                        if not chunk:
                            break
                        out_file.write(chunk)
                        remaining -= len(chunk)

                total_unpacked += 1

        print(f"Total files unpacked: {total_unpacked}")

    except Exception as e:
        print(f"Unpacking error: {e}")


def main():
    print("---------------------------------------------------------------------")
    print("--------------  Universal Packer Unpacker CUI ----------------")
    print("---------------------------------------------------------------------")

    print("Choose operation:")
    print("1. Pack files")
    print("2. Unpack files")
        
    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        pack_files()
    elif choice == "2":
        unpack_files()
    else:
        print("Invalid choice.")

    print("---------------------------------------------------------------------")
    print("--------------- Thank you for using Packer-Unpacker ----------------")
    print("---------------------------------------------------------------------")


if __name__ == "__main__":
    main()
