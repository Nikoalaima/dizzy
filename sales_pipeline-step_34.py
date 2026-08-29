# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: SalesPipeline
class Template:
    def __init__(self, name, stage, amount, probability, notes=None):
        self.name = name
        self.stage = stage
        self.amount = amount
        self.probability = probability
        self.notes = notes

    def apply(self, lead):
        lead.stage = self.stage
        lead.amount = self.amount
        lead.probability = self.probability
        if self.notes:
            lead.notes = self.notes
