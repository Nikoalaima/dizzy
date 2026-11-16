# === Stage 57: Добавь массовое удаление с подтверждением через параметр ===
# Project: SalesPipeline
import json

def mass_delete_leads(confirm_flag, confirm_value, filename="sales_pipeline.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return False, "Файл не найден или повреждён"

    if confirm_flag and not (confirm_flag in data.get("leads", []) and data["leads"][confirm_flag]["confirmed"]):
        return False, "Требуется подтверждение удаления"

    deleted = [lead for lead in data.get("leads", []) if not lead["confirmed"]]
    for lead in deleted:
        data["leads"].remove(lead)

    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True, f"Удалено {len(deleted)} лидов"
    except IOError as e:
        return False, f"Ошибка записи: {e}"
