#!/usr/bin/env python3
"""
Secure Packer/Unpacker (Professional but clean code)
Features:
- Pack/unpack folders recursively
- Optional AES-256 encryption per file
- Compression (zlib)
- Large file support
- Empty folder support
- Automatic packed/unpacked file naming
- Progress bar
- Error logging
- Unpack log inside folder
- User-friendly help
"""

import os
import struct
import zlib
import hashlib
import traceback
from datetime import datetime
from pathlib import Path
from typing import Optional

try:
    from tqdm import tqdm
    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256

# ---------------- CONSTANTS ----------------
HEADER_FORMAT = "<IQQ32s16sQIQB"  # path_len, original_size, compressed_size, salt, nonce, mod_time, perm, checksum, is_dir
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
CHUNK_SIZE = 1024 * 1024  # 1MB
PBKDF2_ITER = 100_000
KEY_LEN = 32
LOG_FILE = "packer_unpacker.log"

# ---------------- LOGGING ----------------
def write_log(msg: str):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")

# ---------------- HELP MENU ----------------
def show_help():
    print("\n" + "="*60)
    print("            SECURE PACKER / UNPACKER HELP")
    print("="*60 + "\n")

    print("1️⃣  PACK A FOLDER")
    print("   - Compress a folder into a single .spack file")
    print("   - Steps:")
    print("       1) Choose option 1 in main menu")
    print("       2) Enter folder path to pack")
    print("       3) Optionally set a password")
    print("   - Output: <folder_name>_packed.spack\n")

    print("2️⃣  UNPACK A .SPACK FILE")
    print("   - Extract all files/folders from a packed file")
    print("   - Steps:")
    print("       1) Choose option 2 in main menu")
    print("       2) Enter packed file name")
    print("       3) Enter password if used")
    print("   - Output: <base_name>_unpacked folder with unpack_log.txt\n")

    print("3️⃣  HELP")
    print("   - Shows this help menu\n")

    print("Notes:")
    print(" - Progress bar shows packing/unpacking progress")
    print(" - Empty folders are preserved")
    print(" - Large files supported")
    print(" - Password input is visible")
    print(" - Errors logged in 'packer_unpacker.log'\n")

    print("Examples:")
    print(" - Packing: 'C:\\Users\\John\\Docs\\backup' → 'backup_packed.spack'")
    print(" - Unpacking: 'backup' → extracts to 'backup_unpacked/'\n")
    print("="*60 + "\n")

# ---------------- KEY DERIVATION ----------------
def get_key(password: str, salt: bytes) -> bytes:
    return PBKDF2(password, salt, dkLen=KEY_LEN, count=PBKDF2_ITER, hmac_hash_module=SHA256)

# ---------------- PROGRESS ----------------
def progress_bar(total_bytes, description=""):
    if HAS_TQDM:
        return tqdm(total=total_bytes, unit="B", unit_scale=True, desc=description)
    else:
        class SimpleProgress:
            def __init__(self, total, desc):
                self.total = max(total, 1)
                self.current = 0
                self.desc = desc
                print(f"{desc}: 0/{total} bytes", end="\r")
            def update(self, n):
                self.current += n
                print(f"{self.desc}: {self.current}/{self.total} bytes", end="\r")
            def close(self):
                print()
        return SimpleProgress(total_bytes, description)

# ---------------- PACK ----------------
def pack_folder(folder_path: str, password: Optional[str] = None):
    folder_path = os.path.abspath(folder_path)
    if not os.path.isdir(folder_path):
        print(f"[ERROR] Folder not found: {folder_path}")
        return

    packed_file = f"{Path(folder_path).name}_packed.spack"
    print(f"[INFO] Packing '{folder_path}' → '{packed_file}'")
    total_entries = 0

    try:
        with open(packed_file, "wb") as out_file:
            for root, dirs, files in os.walk(folder_path):
                rel_root = os.path.relpath(root, folder_path)

                # Empty folder support
                if not files and not dirs:
                    rel_bytes = rel_root.encode()
                    header = struct.pack(HEADER_FORMAT, len(rel_bytes), 0, 0,
                                         b"\x00"*32, b"\x00"*16, 0, 0, 0, 1)
                    out_file.write(header)
                    out_file.write(rel_bytes)
                    total_entries += 1

                # Write directories
                for d in dirs:
                    full_path = os.path.join(root, d)
                    rel_bytes = os.path.relpath(full_path, folder_path).encode()
                    mod_time = int(os.path.getmtime(full_path))
                    perm = os.stat(full_path).st_mode
                    header = struct.pack(HEADER_FORMAT, len(rel_bytes), 0, 0,
                                         b"\x00"*32, b"\x00"*16, mod_time, perm, 0, 1)
                    out_file.write(header)
                    out_file.write(rel_bytes)
                    total_entries += 1

                # Write files
                for f in files:
                    full_path = os.path.join(root, f)
                    rel_bytes = os.path.relpath(full_path, folder_path).encode()
                    orig_size = os.path.getsize(full_path)
                    salt = get_random_bytes(32) if password else b"\x00"*32
                    nonce = get_random_bytes(16) if password else b"\x00"*16
                    key = get_key(password, salt) if password else b"\x00"*32
                    mod_time = int(os.path.getmtime(full_path))
                    perm = os.stat(full_path).st_mode
                    sha = hashlib.sha256()

                    header_pos = out_file.tell()
                    placeholder = struct.pack(HEADER_FORMAT, len(rel_bytes), orig_size, 0, salt, nonce, mod_time, perm, 0, 0)
                    out_file.write(placeholder)
                    out_file.write(rel_bytes)

                    comp = zlib.compressobj(level=6)
                    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce) if password else None
                    comp_size = 0
                    prog = progress_bar(orig_size, f"Packing {rel_bytes.decode()}")
                    with open(full_path, "rb") as in_file:
                        while True:
                            chunk = in_file.read(CHUNK_SIZE)
                            if not chunk:
                                break
                            sha.update(chunk)
                            c_chunk = comp.compress(chunk)
                            if c_chunk:
                                if cipher:
                                    enc_chunk = cipher.encrypt(c_chunk)
                                    out_file.write(enc_chunk)
                                    comp_size += len(enc_chunk)
                                else:
                                    out_file.write(c_chunk)
                                    comp_size += len(c_chunk)
                            prog.update(len(chunk))
                        final = comp.flush()
                        if final:
                            if cipher:
                                out_file.write(cipher.encrypt(final))
                                comp_size += len(final)
                            else:
                                out_file.write(final)
                                comp_size += len(final)
                        if cipher:
                            out_file.write(cipher.digest())
                            comp_size += 16
                    cur_pos = out_file.tell()
                    out_file.seek(header_pos)
                    updated_header = struct.pack(HEADER_FORMAT, len(rel_bytes), orig_size, comp_size,
                                                 salt, nonce, mod_time, perm, int.from_bytes(sha.digest()[:8], 'big'), 0)
                    out_file.write(updated_header)
                    out_file.seek(cur_pos)
                    prog.close()
                    total_entries += 1
        print(f"[DONE] Packed {total_entries} entries → '{packed_file}'")
    except Exception as e:
        write_log(f"Packing error: {e}")
        traceback.print_exc()

# ---------------- UNPACK ----------------
def unpack_file(in_file, out_folder, header_tuple, password: Optional[str]):
    path_len, orig_size, comp_size, salt, nonce, mod_time, perm, checksum, is_dir = header_tuple
    rel_bytes = in_file.read(path_len)
    rel_path = rel_bytes.decode()
    out_path = os.path.join(out_folder, rel_path)

    if is_dir:
        os.makedirs(out_path, exist_ok=True)
        return rel_path, 0, mod_time, perm, True, checksum

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    key = get_key(password, salt) if password else b"\x00"*32
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce) if password else None
    decompress = zlib.decompressobj()
    remaining = comp_size
    sha = hashlib.sha256()
    prog = progress_bar(orig_size, f"Unpacking {rel_path}")

    with open(out_path, "wb") as out_f:
        while remaining > 0:
            read_len = min(CHUNK_SIZE, remaining)
            data = in_file.read(read_len)
            remaining -= len(data)
            if cipher:
                data = cipher.decrypt(data)
            dec = decompress.decompress(data)
            if dec:
                out_f.write(dec)
                sha.update(dec)
            prog.update(len(data))
        final = decompress.flush()
        if final:
            out_f.write(final)
            sha.update(final)
    prog.close()

    if checksum != int.from_bytes(sha.digest()[:8], 'big'):
        write_log(f"[WARNING] Checksum mismatch: {out_path}")

    os.utime(out_path, (mod_time, mod_time))
    os.chmod(out_path, perm)
    return rel_path, orig_size, mod_time, perm, False, checksum

def unpack_folder(packed_file: str, password: Optional[str]):
    candidate = None
    for name in [packed_file, packed_file + ".spack", packed_file + "_packed.spack"]:
        if os.path.exists(name):
            candidate = name
            break
    if candidate is None:
        print(f"[ERROR] File not found: {packed_file}")
        return

    out_folder = os.path.abspath(Path(candidate).stem + "_unpacked")
    os.makedirs(out_folder, exist_ok=True)

    log_path = os.path.join(out_folder, "unpack_log.txt")
    with open(log_path, "w") as log_f:
        log_f.write(f"Unpack Log - {datetime.now()}\n")
        log_f.write("="*80 + "\n")
        log_f.write("Type | Path | Size | ModTime | Permissions | Checksum\n")
        log_f.write("-"*80 + "\n")

        total = 0
        try:
            with open(candidate, "rb") as f:
                while True:
                    header_bytes = f.read(HEADER_SIZE)
                    if not header_bytes:
                        break
                    header_tuple = struct.unpack(HEADER_FORMAT, header_bytes)
                    rel_path, size, mod_time, perm, is_dir, checksum = unpack_file(f, out_folder, header_tuple, password)
                    total += 1
                    mod_str = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d %H:%M:%S")
                    type_str = "DIR " if is_dir else "FILE"
                    log_f.write(f"{type_str} | {rel_path} | {size} | {mod_str} | {oct(perm)} | {checksum}\n")
            print(f"[DONE] Unpacked {total} entries → '{out_folder}'")
            print(f"[INFO] Log saved → {log_path}")
        except Exception as e:
            write_log(f"Unpacking error: {e}")
            traceback.print_exc()

# ---------------- MAIN ----------------
def main():
    print("----- Secure Packer / Unpacker -----")
    print("1. Pack folder")
    print("2. Unpack .spack file")
    print("3. Help")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        folder = input("Folder path to pack: ").strip()
        use_pw = input("Set password? (y/N): ").strip().lower()
        password = None
        if use_pw in ("y","yes"):
            while True:
                pwd = input("Enter password: ")
                pwd2 = input("Confirm password: ")
                if pwd != pwd2:
                    print("Passwords do not match!")
                else:
                    password = pwd
                    break
        pack_folder(folder, password)

    elif choice == "2":
        packed = input("Packed file name: ").strip()
        use_pw = input("Was password used? (y/N): ").strip().lower()
        password = input("Enter password: ") if use_pw in ("y","yes") else None
        unpack_folder(packed, password)

    elif choice == "3":
        show_help()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

