# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: SalesPipeline
def reset_demo_data():
    """Сбросить демо-данные в pipeline к пустому состоянию."""
    global leads, stages, notes
    leads = []
    stages = [
        {"id": 1, "name": "Новый лид", "probability": 0},
        {"id": 2, "name": "Контакт установлен", "probability": 10},
        {"id": 3, "name": "Предложение", "probability": 40},
        {"id": 4, "name": "Договорённость", "probability": 75},
        {"id": 5, "name": "Выигран", "probability": 100},
    ]
    notes = {}

def clear_state():
    """Полная очистка всех данных и сброс на демо."""
    reset_demo_data()
