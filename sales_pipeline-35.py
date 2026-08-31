# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: SalesPipeline
def recommend_next_action(lead):
    """Generate a recommended next action based on lead status, amount, stage, and last activity."""
    if not lead.get('last_activity'):
        return 'schedule_first_contact'
    if lead['last_activity'] > 1000:
        return 'schedule_follow_up'
    if lead['amount'] > 100000:
        return 'schedule_executive_introduction'
    if lead['stage'] == 'closed_won':
        return 'schedule_onboarding'
    if lead['stage'] == 'qualified':
        return 'schedule_demo'
    return 'schedule_qualification_call'
