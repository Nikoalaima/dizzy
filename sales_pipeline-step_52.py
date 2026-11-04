# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: SalesPipeline
def export_report(leads, stages=None):
    stages = stages or list(stages_map.keys())
    total = sum(l['amount'] for l in leads)
    conv = sum(l['amount'] * l['probability'] / 100 for l in leads)
    done = [l for l in leads if l['stage'] in ['won', 'lost']]
    won = sum(l['amount'] for l in done if l['stage'] == 'won')
    lost = sum(l['amount'] for l in done if l['stage'] == 'lost')
    lines = ['Отчёт по продажам', '=' * 40, '', f'Всего лидов: {len(leads)}',
             f'Наблюдаемых: {len(leads) - len(done)}', f'Закрытых: {len(done)}',
             '', 'По этапам:']
    for s in stages:
        items = [l for l in leads if l['stage'] == s]
        if items:
            lines.append(f'  {s}: {len(items)} шт, сумма {sum(l["amount"] for l in items)}')
    lines += ['', f'Общая сумма: {total}', f'Ожидаемые продажи: {conv:.0f}',
              f'Выиграно: {won}', f'Проиграно: {lost}', '']
    return '\n'.join(lines)
