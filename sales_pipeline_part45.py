# === Stage 45: Добавь восстановление из резервной копии ===
# Project: SalesPipeline
import json, os, sys

def load_backup(backup_path):
    if not os.path.exists(backup_path):
        print(f"Error: backup file not found: {backup_path}")
        return None
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            print("Error: invalid backup format")
            return None
        return data
    except Exception as e:
        print(f"Error reading backup: {e}")
        return None

def restore_from_backup(backup_path, file_path):
    data = load_backup(backup_path)
    if data is None:
        return False
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Restored {file_path} from {backup_path}")
    return True

if __name__ == "__main__":
    if len(sys.argv) == 3:
        restore_from_backup(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python script.py <backup_file> <target_file>")
