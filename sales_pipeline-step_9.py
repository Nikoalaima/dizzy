# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: SalesPipeline
import json, sys
try:
    initial_data = """
{
  "stages": [
    {"id": 1, "name": "Новый лид", "probability": 0.1},
    {"id": 2, "name": "Квалификация", "probability": 0.3},
    {"id": 3, "name": "Презентация", "probability": 0.5},
    {"id": 4, "name": "Сделка", "probability": 1.0}
  ],
  "leads": [
    {
      "id": 101,
      "name": "ООО Ромашка",
      "stage_id": 1,
      "amount": 50000,
      "probability": 0.1,
      "notes": "Первичный контакт"
    },
    {
      "id": 102,
      "name": "ИП Иванов",
      "stage_id": 3,
      "amount": 120000,
      "probability": 0.5,
      "notes": "Интерес к пакету Pro"
    }
  ]
}"""
    pipeline = json.loads(initial_data)
except json.JSONDecodeError as e:
    print(f"Ошибка парсинга JSON: {e}", file=sys.stderr)
    sys.exit(1)

# Проверка целостности данных и установка вероятностей по умолчанию для лида
for lead in pipeline["leads"]:
    stage = next((s for s in pipeline["stages"] if s["id"] == lead["stage_id"]), None)
    if stage:
        lead["probability"] = stage["probability"]

# Вывод загруженных данных для проверки
print(f"Загружено {len(pipeline['leads'])} лидов и {len(pipeline['stages'])} этапов.")
