# === Stage 39: Добавь документационную строку с описанием сценариев использования ===
# Project: SalesPipeline
def demo_scenarios():
    """
    Демонстрация сценариев использования SalesPipeline:
    1. Создание лида с базовыми данными
    2. Добавление заметки к лиду
    3. Перемещение лида на следующий этап воронки
    4. Обновление суммы сделки с учётом вероятности
    5. Просмотр всех лидов с их статусами
    6. Подведение итогов по этапам воронки
    """
    pipeline = SalesPipeline()

    # Сценарий 1: Регистрация нового лида
    lead = {
        "id": 1,
        "company": "TechCorp",
        "contact": "Иван Иванов",
        "email": "ivan@techcorp.com",
        "phone": "+7-900-123-4567",
        "stage": "Новый",
        "amount": 500000,
        "probability": 0.1,
        "notes": "Первый контакт на выставке",
        "created_at": "2024-01-15",
    }
    pipeline.add_lead(lead)
    print(f"✓ Лид добавлен: {lead['company']}")

    # Сценарий 2: Добавление заметки
    pipeline.add_note(lead["id"], "Интересовался тарифом Enterprise")
    print(f"✓ Заметка добавлена к {lead['company']}")

    # Сценарий 3: Перемещение на этап "Рассмотрение"
    pipeline.move_lead(lead["id"], "Рассмотрение")
    print(f"✓ Лид перемещён на этап: {lead['stage']}")

    # Сценарий 4: Обновление суммы и вероятности
    pipeline.update_lead(lead["id"], amount=450000, probability=0.3)
    print(f"✓ Сумма обновлена: {lead['amount']:,} руб., вероятность: {lead['probability']:.0%}")

    # Сценарий 5: Просмотр всех лидов
    print("\n--- Текущие лиды ---")
    for l in pipeline.get_leads():
        print(f"  [{l['stage']}] {l['company']} — {l['amount']:,} руб. ({l['probability']:.0%})")

    # Сценарий 6: Итоги по этапам
    print("\n--- Статистика по этапам ---")
    for stage, leads in pipeline.get_stages().items():
        total = sum(l["amount"] for l in leads)
        print(f"  {stage}: {len(leads)} лидов, сумма: {total:,} руб.")

    print("\n✓ Демонстрация завершена.")

if __name__ == "__main__":
    demo_scenarios()
