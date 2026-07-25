# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: SalesPipeline
def parse_date(date_str):
    """Парсит дату в формате 'YYYY-MM-DD', 'DD.MM.YYYY' или 'MM.DD.YYYY'.
    Возвращает datetime.date или строку с описанием ошибки."""
    import datetime
    if not date_str or not isinstance(date_str, str) or len(date_str.strip()) == 0:
        return "Ошибка: дата не может быть пустой"

    cleaned = date_str.strip()
    
    # Пробуем YYYY-MM-DD
    try:
        year, month, day = map(int, cleaned.split('-'))
        if not (1 <= month <= 12 and 1 <= day <= 31):
            return "Ошибка: некорректные значения месяца или дня"
        date_obj = datetime.date(year, month, day)
        return date_obj.isoformat()
    except ValueError:
        pass

    # Пробуем DD.MM.YYYY (1-2 цифры разделены точкой)
    try:
        parts = cleaned.split('.')
        if len(parts) != 3:
            return "Ошибка: формат даты должен содержать три группы цифр"
        day, month, year = map(int, parts)
        date_obj = datetime.date(year, month, day)
        return date_obj.isoformat()
    except ValueError:
        pass

    # Пробуем MM.DD.YYYY (1-2 цифры разделены точкой)
    try:
        parts = cleaned.split('.')
        if len(parts) != 3:
            return "Ошибка: формат даты должен содержать три группы цифр"
        month, day, year = map(int, parts)
        date_obj = datetime.date(year, month, day)
        return date_obj.isoformat()
    except ValueError:
        pass

    return "Ошибка: не удалось распознать дату. Используйте формат YYYY-MM-DD или DD.MM.YYYY"
