# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: SalesPipeline
def generate_summary(leads):
    if not leads:
        return "Сводка: нет данных"
    
    total_value = sum(l["amount"] for l in leads)
    closed_leads = [l for l in leads if l.get("stage") == "Closed Won"]
    open_leads = len(leads) - len(closed_leads)
    avg_probability = sum(l["probability"] for l in leads) / len(leads)
    
    summary = f"Итого лидов: {len(leads)}\nОткрыто: {open_leads}, Закрыто: {len(closed_leads)}\nОбщая сумма: {total_value}\nСредняя вероятность: {avg_probability:.1f}%\n"
    
    return summary
