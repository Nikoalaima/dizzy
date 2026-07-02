# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: SalesPipeline
import json, os

def save_pipeline(data: dict) -> None:
    file_path = "sales_data.json"
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"[Ошибка] Не удалось сохранить файл {file_path}: {e}")

def load_pipeline() -> dict:
    file_path = "sales_data.json"
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("[Предупреждение] Файл JSON повреждён или пуст. Создаётся новый.")
    return {"leads": [], "stages": []}
