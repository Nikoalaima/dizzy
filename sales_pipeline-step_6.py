# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: SalesPipeline
def filter_leads(status=None, category=None, tags=None):
    filtered = []
    for lead in leads:
        if status and lead.get('status') != status:
            continue
        if category and lead.get('category') != category:
            continue
        if tags is not None:
            lead_tags = set(lead.get('tags', []))
            if not any(tag in lead_tags for tag in tags):
                continue
        filtered.append(lead)
    return filtered

def search_leads(query=None, limit=10):
    results = []
    query_lower = query.lower() if query else ''
    for lead in leads:
        text = f"{lead.get('name', '')} {lead.get('company', '')}".lower()
        notes = ' '.join(lead.get('notes', [])).lower()
        tags_str = ' '.join(lead.get('tags', [])).lower()
        if query_lower in text or query_lower in notes or query_lower in tags_str:
            results.append(lead)
            if len(results) >= limit:
                break
    return results
