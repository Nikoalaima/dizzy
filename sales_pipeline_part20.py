# === Stage 20: Добавь восстановление записей из архива ===
# Project: SalesPipeline
def archive_to_records(archive_path):
    """Restore records from the archive file and return them as a list of dicts."""
    if not os.path.exists(archive_path):
        print(f"Archive not found: {archive_path}")
        return []
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, dict) and 'records' in data:
            records = data['records']
        elif isinstance(data, list):
            records = data
        else:
            print("Unexpected archive format")
            return []
        valid_records = [r for r in records if all(k in r for k in ('name', 'amount', 'stage') and r['amount'] > 0)]
        print(f"Restored {len(valid_records)} records from archive.")
        return valid_records
    except Exception as e:
        print(f"Error reading archive: {e}")
        return []

def save_archive(records, archive_path):
    """Save current records to the archive file for future restoration."""
    with open(archive_path, 'w', encoding='utf-8') as f:
        json.dump({'records': records}, f, ensure_ascii=False)
    print(f"Archived {len(records)} records.")

# Example usage:
# archived = save_archive(records_to_backup, 'pipeline_archive.json')
# restored = archive_to_records('pipeline_archive.json')
