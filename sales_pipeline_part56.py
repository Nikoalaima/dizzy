# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: SalesPipeline
def bulk_update_records():
    print("Выберите записи для массового обновления:")
    selected = []
    for idx, lead in enumerate(leads):
        print(f"{idx}: {lead['name']} ({lead['stage']}, {lead['amount']} ₽)")
    choices = input("Введите индексы через пробел (или 'q' для отмены): ")
    if choices.strip().lower() == 'q':
        return
    for c in choices.split():
        if c.isdigit() and int(c) < len(leads):
            selected.append(leads[int(c)])
    if not selected:
        print("Ничего не выбрано.")
        return
    print(f"\nВыбрано записей: {len(selected)}")
    print("Укажите новые значения:")
    new_stage = input("Этап: ").strip()
    try:
        new_amount = int(input("Сумма (₽): "))
    except ValueError:
        new_amount = leads[0]['amount']
    new_prob = input("Вероятность (%): ").strip()
    try:
        new_prob = int(new_prob)
    except ValueError:
        new_prob = leads[0]['probability']
    note = input("Заметка: ").strip()
    for lead in selected:
        lead['stage'] = new_stage
        lead['amount'] = new_amount
        lead['probability'] = new_prob
        if note:
            lead['notes'] = note
    print("Массовое обновление завершено.")
