# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: SalesPipeline
def sort_leads(key='date', reverse=False):
    if key == 'date':
        return sorted(leads, key=lambda x: x.get('created_at') or '', reverse=reverse)
    elif key == 'priority':
        priority_map = {'high': 0, 'medium': 1, 'low': 2}
        return sorted(leads, key=lambda x: priority_map.get(x.get('priority', 'medium'), 1), reverse=(key != 'priority'))
    else:
        return sorted(leads, key=lambda x: (x.get(key) or '').lower(), reverse=reverse)
