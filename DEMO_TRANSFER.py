import os
import json
import zstandard as zstd
import time
import sys
from datetime import datetime

CONFIG_FILE = "config.json"

def console_print(message, end='\n'):
    """Print with immediate flush for .exe compatibility"""
    print(message, end=end, flush=True)
    # Additional flush for Windows .exe files
    if sys.platform.startswith('win'):
        try:
            sys.stdout.flush()
            sys.stderr.flush()
        except:
            pass

def decompress_zst(src_path, dest_path):
    """Decompress a .zst file to .dem"""
    with open(src_path, 'rb') as compressed, open(dest_path, 'wb') as decompressed:
        dctx = zstd.ZstdDecompressor()
        dctx.copy_stream(compressed, decompressed)

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return None

def save_config(source, destination):
    with open(CONFIG_FILE, "w") as f:
        json.dump({"source": source, "destination": destination}, f, indent=4)

def get_or_create_config():
    config = load_config()
    if config:
        console_print(f"\n[OK] Loaded saved folders:")
        console_print(f"   Source: {config['source']}")
        console_print(f"   Destination: {config['destination']}")
        change = input("Do you want to change them? (y/N): ").strip().lower()
        if change != "y":
            return config

    source = input("Enter SOURCE folder path (where .zst files appear): ").strip('" ')
    destination = input("Enter DESTINATION folder path (CS2 folder): ").strip('" ')
    save_config(source, destination)
    console_print("[OK] Saved paths for next time!\n")
    return {"source": source, "destination": destination}

def is_file_stable(path, wait_time=3):
    """Check if file is no longer growing in size"""
    try:
        initial_size = os.path.getsize(path)
        time.sleep(wait_time)
        return os.path.getsize(path) == initial_size
    except FileNotFoundError:
        return False

def process_zst_file(file_path, dest_folder):
    """Process one .zst file"""
    try:
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        new_name = f"demo_{timestamp}.dem"
        dest_path = os.path.join(dest_folder, new_name)
        decompress_zst(file_path, dest_path)
        console_print(f"[OK] Transferred to: {dest_path}")
        os.remove(file_path)
        console_print(f"[DEL] Deleted original: {file_path}")
    except Exception as e:
        console_print(f"[ERR] Error processing {file_path}: {e}")

def watch_folder(source_folder, dest_folder):
    """Continuously watch for new .zst files"""
    console_print(f"\n[INFO] Watching folder:\n{source_folder}\n")
    console_print("Press Ctrl + C to stop.\n")

    processed = set()

    while True:
        try:
            for file_name in os.listdir(source_folder):
                if not file_name.lower().endswith(".zst"):
                    continue

                full_path = os.path.join(source_folder, file_name)
                if full_path in processed:
                    continue

                # Wait until file is fully downloaded and stable
                console_print(f"[SCAN] Checking file: {file_name}")
                if is_file_stable(full_path, wait_time=3):
                    console_print(f"\n[NEW] Found new demo: {file_name}")
                    process_zst_file(full_path, dest_folder)
                    processed.add(full_path)
                else:
                    console_print(f"[WAIT] {file_name} still downloading...")

            time.sleep(5)
        except KeyboardInterrupt:
            console_print("\n[EXIT] Stopped watching folder. Goodbye!")
            break
        except Exception as e:
            console_print(f"[WARN] Error while watching folder: {e}")
            time.sleep(5)

if __name__ == "__main__":
    # Set console encoding for Windows and force unbuffered output
    if sys.platform.startswith('win'):
        os.system('chcp 65001 >nul 2>&1')  # Set UTF-8 encoding
    
    # Set environment variable for unbuffered output (works with PyInstaller)
    os.environ['PYTHONUNBUFFERED'] = '1'
        
    console_print("=== Faceit Demo Auto Transfer Tool ===")
    input("Press Enter to start...")

    config = get_or_create_config()
    os.makedirs(config["destination"], exist_ok=True)

    watch_folder(config["source"], config["destination"])