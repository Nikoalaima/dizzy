# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: SalesPipeline
def weekly_stats(leads):
    """Return dict of week_start_date -> {count, total_value, avg_probability}."""
    from datetime import date, timedelta
    weeks = {}
    for lead in leads:
        d = date(lead['date'])
        w = (d - timedelta(days=d.weekday())).isoformat()  # Monday
        if w not in weeks:
            weeks[w] = {'count': 0, 'total_value': 0.0, 'avg_probability': 0.0}
        weeks[w]['count'] += 1
        weeks[w]['total_value'] += float(lead.get('value', 0))
    for w in weeks:
        if weeks[w]['count']:
            weeks[w]['avg_probability'] = sum(l['probability'] for l in leads if date(lead['date']).isocalendar()[1] == (date.fromisoformat(w).isocalendar()[1])) / weeks[w]['count']
    return weeks
