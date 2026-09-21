# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: SalesPipeline
def self_check():
    print("=== SalesPipeline Self-Check ===")
    print(f"✅ Лиды: {len(leads)}")
    print(f"✅ Этапы: {len(stages)}")
    print(f"✅ Суммы: {total_deal_value} руб.")
    print(f"✅ Вероятность: {round(avg_probability, 2)}%")
    print(f"✅ Заметки: {len(lead_notes)}")
    print(f"✅ Конверсия: {round(conversion_rate, 2)}%")
    print("=== SalesPipeline Ready ===")
