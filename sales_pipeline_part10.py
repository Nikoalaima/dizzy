# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: SalesPipeline
def export_to_json():
    import json
    data = {
        "leads": leads,
        "stages": stages,
        "stage_order": stage_order,
        "settings": settings
    }
    return json.dumps(data, indent=2, ensure_ascii=False)
