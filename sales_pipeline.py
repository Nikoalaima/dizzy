# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: SalesPipeline
import json, os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "leads.json"

def load_leads():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_leads(leads):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(leads, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    demo_data = [
        {"id": 101, "company": "ООО Ромашка", "stage": "Новый лид", "amount": 50000, "probability": 10, "notes": ""},
        {"id": 102, "company": "ИП Иванов", "stage": "Переговоры", "amount": 120000, "probability": 40, "notes": "Ждем КП"},
    ]
    save_leads(demo_data)
    print(f"Демо-данные загружены в {DATA_FILE}")
