# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: SalesPipeline
def _check_overdue_reminders(self):
        overdue = []
        for lead in self._leads:
            if not lead.reminder or lead.reminder.date <= datetime.now().date():
                overdue.append(lead)
        return overdue
