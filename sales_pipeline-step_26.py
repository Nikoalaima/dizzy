# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: SalesPipeline
def demo_run():
    print("=== SalesPipeline Demo ===")
    for lead in leads:
        print(f"  {lead['name']} | Stage: {lead['stage']['name']} | Prob: {lead['probability']:.0f}% | Value: ${lead['value']:,.2f}")
    print("\n--- Quick Actions ---")
    for cmd in demo_commands():
        print(cmd)

def demo_commands():
    return [
        "create_lead(name='Acme Corp', stage=stages[1], value=50000, prob=60)",
        "update_stage(lead_id=0, stage=stages[2])",
        "add_note(lead_id=0, note='Follow up next week')",
        "calculate_pipeline_value()",
    ]

demo_run()
