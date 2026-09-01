# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: SalesPipeline
def repair_and_verify(leads):
    """Проверяет целостность данных и автоматически чинит типичные проблемы.

    Возвращает:
      - count_leads: количество лидов после ремонта
      - issues_fixed: список описаний исправленных проблем
    """
    issues_fixed = []
    repaired = []

    for lead in leads:
        repaired_lead = dict(lead)

        # Проверка 1: сумма должна быть числом >= 0
        if not isinstance(repaired_lead.get('amount'), (int, float)):
            try:
                repaired_lead['amount'] = float(repaired_lead['amount'])
                issues_fixed.append(f"amount='{repaired_lead['amount']}' исправлен из строки")
            except (ValueError, TypeError):
                repaired_lead['amount'] = 0.0
                issues_fixed.append(f"amount='{repaired_lead['amount']}' установлен в 0")

        # Проверка 2: вероятность должна быть числом от 0 до 100
        prob = repaired_lead.get('probability')
        if prob is None:
            prob = 50
        elif not isinstance(prob, (int, float)):
            try:
                prob = float(prob)
                issues_fixed.append(f"probability='{prob}' исправлен из строки")
            except (ValueError, TypeError):
                prob = 50
                issues_fixed.append(f"probability='{prob}' установлен в 50")
        repaired_lead['probability'] = max(0.0, min(100.0, prob))

        # Проверка 3: stage_id должен быть строкой или числом
        stage_id = repaired_lead.get('stage_id')
        if stage_id is None:
            stage_id = '1'
        repaired_lead['stage_id'] = str(stage_id)

        # Проверка 4: email не должен быть пустым
        email = repaired_lead.get('email', '')
        if isinstance(email, str) and not email.strip():
            repaired_lead['email'] = 'unknown@example.com'
            issues_fixed.append(f"email='{email}' заменён на 'unknown@example.com'")

        repaired.append(repaired_lead)

    return len(repaired), issues_fixed
