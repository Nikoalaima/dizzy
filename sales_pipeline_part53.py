# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: SalesPipeline
def import_leads_from_text(filename):
    """Читает лиды из текстового файла в формате CSV.

    Формат строк: id,name,stage,amount,probability,notes
    Пример:  1,Иван Петров,Квалификация,500000,20,Первый контакт
    """
    leads = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split(",")
                if len(parts) < 5:
                    continue
                lead_id, name, stage, amount, probability = parts[:5]
                notes = ",".join(parts[5:]) if len(parts) > 5 else ""
                try:
                    amount = float(amount)
                    probability = float(probability)
                except ValueError:
                    continue
                leads.append({
                    "id": int(lead_id),
                    "name": name,
                    "stage": stage,
                    "amount": amount,
                    "probability": probability,
                    "notes": notes,
                })
        return leads
    except FileNotFoundError:
        return None
