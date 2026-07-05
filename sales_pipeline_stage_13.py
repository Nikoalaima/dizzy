# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: SalesPipeline
def search_leads(query: str) -> list[dict]:
    if not query.strip():
        return []
    q = query.lower()
    results = [lead for lead in leads_data if (q in lead.get('name', '').lower() or 
                                                q in lead.get('company', '').lower() or 
                                                q in lead.get('phone', '').lower())]
    return results
