# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: SalesPipeline
def print_metrics(leads):
    """Print key metrics for the sales pipeline."""
    if not leads:
        print("No leads to analyze.")
        return
    
    total = len(leads)
    active = sum(1 for l in leads if l.get('status') != 'closed')
    closed = total - active
    
    total_value = sum(l.get('amount', 0) for l in leads)
    expected_revenue = sum(l.get('amount', 0) * (l.get('probability', 0) / 100.0) for l in leads if l.get('status') != 'closed')
    
    stages = {}
    for l in leads:
        stage = l.get('stage', 'Unknown')
        stages[stage] = stages.get(stage, 0) + 1
    
    print(f"Total Leads: {total}")
    print(f"Active: {active} | Closed: {closed}")
    print(f"Pipeline Value: ${total_value:.2f}")
    print(f"Expected Revenue: ${expected_revenue:.2f}")
    
    sorted_stages = sorted(stages.items(), key=lambda x: -x[1])
    print("Leads by Stage:")
    for stage, count in sorted_stages:
        print(f"  {stage}: {count}")
