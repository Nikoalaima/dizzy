# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: SalesPipeline
def polish_pipeline():
    """Final polish: clean up messages, names, and comments."""
    sales_pipeline = SalesPipeline(
        stages=[
            {"name": "Новый лид", "probability": 0.0, "color": "#888888"},
            {"name": "Квалификация", "probability": 0.25, "color": "#4CAF50"},
            {"name": "Демо", "probability": 0.50, "color": "#2196F3"},
            {"name": "Предложение", "probability": 0.75, "color": "#FF9800"},
            {"name": "Закрыт-выигран", "probability": 1.0, "color": "#4CAF50"},
            {"name": "Закрыт-проигран", "probability": 0.0, "color": "#F44336"},
        ]
    )
    sales_pipeline.add_lead(
        name="Алексей Иванов",
        company="Техно-Групп",
        email="alex@techno.ru",
        phone="+79001234567",
        amount=150000,
        stage="Новый лид",
        notes="Интересует CRM-система для отдела продаж",
    )
    sales_pipeline.add_lead(
        name="Мария Петрова",
        company="Старт-Ап",
        email="maria@startup.io",
        phone="+79007654321",
        amount=75000,
        stage="Квалификация",
        notes="Сравняет нас с конкурентами, ждет демо",
    )
    sales_pipeline.add_lead(
        name="Дмитрий Сидоров",
        company="МегаКорп",
        email="dima@megacorp.com",
        phone="+79001112233",
        amount=500000,
        stage="Демо",
        notes="Провели демо, клиент доволен, ждёт предложение",
    )
    sales_pipeline.add_lead(
        name="Елена Козлова",
        company="ЛайтСофт",
        email="elena@lightsoft.net",
        phone="+79004445566",
        amount=200000,
        stage="Предложение",
        notes="Отправили КП, ждём ответ через 5 дней",
    )
    sales_pipeline.add_lead(
        name="Иван Волков",
        company="Вектор",
        email="ivan@vector.org",
        phone="+79008889900",
        amount=0,
        stage="Закрыт-выигран",
        notes="Сделка закрыта, подписан контракт на 3 месяца",
    )
    sales_pipeline.add_lead(
        name="Ольга Никитина",
        company="Нова",
        email="olga@nova.biz",
        phone="+79003334455",
        amount=0,
        stage="Закрыт-проигран",
        notes="Клиент выбрал конкурента, бюджет закрыли",
    )

    print("=" * 60)
    print("📊 ОТЧЁТ SALES PIPELINE — ПОСЛЕ ФИНАЛЬНОЙ ПОЛИРОВКИ")
    print("=" * 60)
    sales_pipeline.display()
    print("\n📈 АНАЛИТИКА:")
    sales_pipeline.analyze()
    print("\n💰 РЕКОМЕНДАЦИИ:")
    sales_pipeline.recommend()
    print("\n📋 ЗДЕСЬ ДЕТАЛИ:")
    sales_pipeline.details()
    print("\n📜 ИСТОРИЯ ЛЕДА (пример):")
    sales_pipeline.history()
