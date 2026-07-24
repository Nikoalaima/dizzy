# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: SalesPipeline
def format_lead(lead):
    """Компактный вывод одной записи лидо."""
    parts = [f"ID: {lead['id']}", f"Имя: {lead.get('name', '—')}", 
             f"E-mail: {lead.get('email', '—')}", f"Источник: {lead.get('source', '—')}"]
    if lead.get("phone"): parts.append(f"Tel: {lead['phone']}")
    if "notes" in lead and lead["notes"]: parts.append(f"Замечания: {lead['notes']}")
    if lead.get("amount"): parts.append(f"Сумма: {lead['amount']:,} руб.")
    if lead.get("probability"): parts.append(f"Вероятность: {lead['probability']}%")
    stage = lead.get("stage", {})
    if isinstance(stage, str): stage = {"name": stage}
    line = f"\n=== Лид ===\n  Этап: {stage.get('name', '—')}"
    return "\n".join(parts) + line
