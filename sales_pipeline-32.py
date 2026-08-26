# === Stage 32: Добавь журнал действий пользователя ===
# Project: SalesPipeline
class UserAction:
    def __init__(self, user, action, target_id=None, details=""):
        self.user = user
        self.action = action
        self.target_id = target_id
        self.details = details
        self.timestamp = datetime.now()

    def __repr__(self):
        target = self.target_id or "-"
        return f"[{self.timestamp}] {self.user}: {self.action} {target} — {self.details}"

class ActionLog:
    def __init__(self):
        self._entries = []

    def log(self, user, action, target_id=None, details=""):
        self._entries.append(UserAction(user, action, target_id, details))

    def show(self):
        if not self._entries:
            return "Журнал пуст."
        return "\n".join(str(e) for e in self._entries)
