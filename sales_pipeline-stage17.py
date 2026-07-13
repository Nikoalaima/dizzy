# === Stage 17: Добавь группировку записей по категориям ===
# Project: SalesPipeline
def group_by_category(records, category_field='category'):
    """Группирует записи по указанному полю категории."""
    groups = {}
    for rec in records:
        cat = rec.get(category_field) or 'Uncategorized'
        if cat not in groups:
            groups[cat] = []
        groups[cat].append(rec)
    return groups

def format_groups(groups, max_records=3):
    """Форматирует группы в читаемый текст."""
    result = []
    for cat, recs in groups.items():
        lines = [f"  Категория: {cat}"]
        shown = 0
        for r in recs[:max_records]:
            if isinstance(r, dict):
                line_parts = [f"- {r.get('name', 'без имени')}" ]
                if 'amount' in r and r['amount']:
                    line_parts.append(f" ({r['amount']})")
                lines.append(" ".join(line_parts))
                shown += 1
        if len(recs) > max_records:
            lines.append(f"  ... и ещё {len(recs)-max_records} записей")
        result.append("\n".join(lines))
    return "\n\n".join(result)

def categorize_leads(leads):
    """Авто-категоризация лидов по сумме: малые, средние, крупные."""
    rules = [
        ('Крупные', lambda x: x.get('amount', 0) >= 100),
        ('Средние', lambda x: 50 <= x.get('amount', 0) < 100),
        ('Малые', lambda x: x.get('amount', 0) < 50),
    ]
    result = {}
    for lead in leads:
        cat = 'Малые'
        for c, rule in rules:
            if rule(lead):
                cat = c
                break
        result.setdefault(cat, []).append(lead)
    return result
