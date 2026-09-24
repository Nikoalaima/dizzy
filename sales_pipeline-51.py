# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: SalesPipeline
class AuditLog:
    def __init__(self):
        self.entries = []

    def log(self, action, entity_type, entity_id, old_value=None, new_value=None):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "old_value": old_value,
            "new_value": new_value,
        }
        self.entries.append(entry)
        return entry
