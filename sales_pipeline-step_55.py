# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: SalesPipeline
def _find_similar_lead(lead, pipeline):
    matches = []
    for existing in pipeline:
        if existing["id"] == lead["id"]:
            continue
        if existing["name"].lower() != lead["name"].lower():
            continue
        if lead["value"] > 0 and existing["value"] > 0:
            if abs(lead["value"] - existing["value"]) / max(lead["value"], existing["value"]) > 0.2:
                continue
        if lead["stage"] != existing["stage"]:
            continue
        if lead["probability"] != existing["probability"]:
            continue
        matches.append(existing)
    return matches


def find_duplicate_lead(lead, pipeline):
    matches = _find_similar_lead(lead, pipeline)
    if matches:
        return matches[0]
    return None
