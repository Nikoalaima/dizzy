# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: SalesPipeline
def monthly_stats(leads):
    from collections import defaultdict
    stats = {}
    for lead in leads:
        date_str = lead.get("created_at", "")[:7]  # YYYY-MM
        if date_str not in stats:
            stats[date_str] = {"count": 0, "amount": 0.0}
        stats[date_str]["count"] += 1
        val = float(lead.get("deal_value", 0)) * (lead.get("probability", 1) / 100)
        stats[date_str]["amount"] += val
    return stats
