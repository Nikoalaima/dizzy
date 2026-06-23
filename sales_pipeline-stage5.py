# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: SalesPipeline
def delete_lead(lead_id: int) -> bool:
    """Удаление лида по ID с проверкой существования."""
    if lead_id not in leads_db:
        print(f"Лид #{lead_id} не найден.")
        return False
    
    del leads_db[lead_id]
    print(f"Лид #{lead_id} успешно удален.")
    return True

def delete_stage(stage_name: str) -> bool:
    """Удаление стадии воронки с проверкой использования."""
    if stage_name not in stages_db:
        print(f"Стадия '{stage_name}' не найдена.")
        return False
    
    used_in = [lid for lid, data in leads_db.items() if data.get('stage') == stage_name]
    if used_in:
        print(f"Невозможно удалить стадию '{stage_name}': она используется лидами {used_in}.")
        return False
    
    del stages_db[stage_name]
    print(f"Стадия '{stage_name}' успешно удалена.")
    return True
