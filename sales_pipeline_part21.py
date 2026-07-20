# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: SalesPipeline
def add_reminder(lid, note):
    """Adds a simple reminder (date + message) to a lead."""
    lid.reminders.append({"note": note})
