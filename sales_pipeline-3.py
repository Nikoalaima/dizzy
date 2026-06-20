# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: SalesPipeline
from typing import List, Dict, Optional

class Lead:
    def __init__(self, name: str, company: str, stage: int = 0, amount: float = 0.0, probability: float = 10.0, notes: str = ""):
        self.name = name
        self.company = company
        self.stage = stage
        self.amount = amount
        self.probability = probability
        self.notes = notes

class SalesPipeline:
    def __init__(self):
        self.leads: List[Lead] = []
    
    def add_lead(self, name: str, company: str, stage: int = 0, amount: float = 0.0, probability: float = 10.0, notes: str = "") -> Lead:
        lead = Lead(name, company, stage, amount, probability, notes)
        self.leads.append(lead)
        return lead

    def get_total_pipeline_value(self) -> float:
        return sum(l.amount * l.probability / 100 for l in self.leads)
