# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: SalesPipeline
class Lead:
    def __init__(self, name, company, stage='Новый', value=0, probability=25, notes=''):
        self.name = name.strip() if isinstance(name, str) else ''
        self.company = company.strip() if isinstance(company, str) else ''
        self.stage = stage
        self.value = float(value) if isinstance(value, (int, float)) and value >= 0 else 0.0
        self.probability = int(probability) if isinstance(probability, int) and 1 <= probability <= 100 else 25
        self.notes = notes.strip() if isinstance(notes, str) else ''

    def to_dict(self):
        return {k: v for k, v in vars(self).items()}

def validate_input(name, company, stage='Новый', value=0, probability=25, notes=''):
    errors = []
    if not name or len(name) > 100: errors.append("Имя должно быть от 1 до 100 символов")
    if not company or len(company) > 100: errors.append("Компания должна быть от 1 до 100 символов")
    valid_stages = ['Новый', 'Контакт', 'Предложение', 'Переговоры', 'Выигрыш', 'Проигрыш']
    if stage not in valid_stages: errors.append(f"Этап должен быть одним из: {', '.join(valid_stages)}")
    try:
        val = float(value)
        if val < 0 or val > 1e9: errors.append("Сумма должна быть от 0 до 1 млрд")
    except ValueError: errors.append("Некорректная сумма")
    if not (1 <= probability <= 100): errors.append("Вероятность должна быть от 1% до 100%")
    return errors

def create_lead(name, company, stage='Новый', value=0, probability=25, notes=''):
    errors = validate_input(name, company, stage, value, probability, notes)
    if errors: raise ValueError('\n'.join(errors))
    return Lead(name, company, stage, value, probability, notes)
