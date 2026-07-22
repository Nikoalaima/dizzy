# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: SalesPipeline
def print_sales_table(leads):
    """Отображает таблицу лидов в консоль."""
    if not leads:
        print("Нет данных для отображения.")
        return
    
    # Определяем ширину полей
    width_lead = max(len(l['name']) for l in leads) + 2 if leads else 10
    width_stage = max(len(l['stage'] or 'N/A') for l in leads) + 2
    width_amount = max(len(f"${l.get('amount', 0):,.0f}") for l in leads) + 2
    width_probability = max(len(str(l.get('probability', 0))) for l in leads) + 4
    
    # Заголовки таблицы
    header = f"{'Имя':<{width_lead}} | {'Этап':<{width_stage}} | {'Сумма':^{width_amount}} | {'Вероятность':>{width_probability}}"
    
    print(f"\n{'='*len(header)}")
    print(header)
    print(f"{'='*len(header)}")
    
    # Строки таблицы
    for lead in leads:
        name = lead.get('name', 'N/A')
        stage = lead.get('stage', 'N/A') or 'N/A'
        amount = f"${lead.get('amount', 0):,.2f}" if isinstance(lead.get('amount'), (int, float)) else str(lead.get('amount', 'N/A'))
        probability = f"{lead.get('probability', 0)}%" if lead.get('probability') is not None else "N/A"
        
        row = f"{name:<{width_lead}} | {stage:<{width_stage}} | {amount:^{width_amount}} | {probability:>12}"
        print(row)
    
    # Подвал таблицы
    total_leads = len(leads)
    total_amount = sum(lead.get('amount', 0) for lead in leads if isinstance(lead.get('amount'), (int, float)))
    total_probability = sum(lead.get('probability', 0) for lead in leads if lead.get('probability') is not None and isinstance(lead['probability'], int))
    
    footer = f"{'='*len(header)}\nИтого: {total_leads} лидов | Общая сумма: ${total_amount:,.2f} | Средняя вероятность: {total_probability/total_leads:.1f}% (если доступно)\n{'='*len(header)}"
    print(footer)

# Пример использования:
# leads = [
#     {'name': 'Иван Петров', 'stage': 'Новый', 'amount': 5000, 'probability': None},
#     {'name': 'Мария Сидорова', 'stage': 'Переговоры', 'amount': 12000, 'probability': 60},
#     {'name': 'Алексей Козлов', 'stage': 'Закрыто', 'amount': 35000, 'probability': 100}
# ]
# print_sales_table(leads)
