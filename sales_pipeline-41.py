# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: SalesPipeline
def dry_run_mode(enabled: bool = True):
    global _dry_run
    _dry_run = enabled
    if enabled:
        print("[DRY-RUN] Все операции изменения будут записаны в лог вместо выполнения.")
        return True
    return False

def _log_dry_run(operation: str, details: dict):
    print(f"[DRY-RUN LOG] {operation} | {details}")
    return None

def _simulate_update(records: list, field: str, value, record_id: str):
    if _dry_run:
        return _log_dry_run(f"UPDATE {record_id} field={field} value={value}", {"record_id": record_id, "field": field, "value": value})
    for rec in records:
        if rec.get("id") == record_id:
            rec[field] = value
            return rec
    return None

def _simulate_delete(records: list, record_id: str):
    if _dry_run:
        return _log_dry_run(f"DELETE {record_id}", {"record_id": record_id})
    return [r for r in records if r.get("id") != record_id]
