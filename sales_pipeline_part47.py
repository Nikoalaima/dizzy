# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: SalesPipeline
def demo():
    """Показывает основной пользовательский сценарий: создание лида, перемещение по этапам, добавление заметки и расчёт итоговой суммы."""
    pipeline = Pipeline()
    pipeline.add_stage("Новый лид", 0.1)
    pipeline.add_stage("Контакт", 0.2)
    pipeline.add_stage("Демо", 0.3)
    pipeline.add_stage("Прогноз", 0.5)
    pipeline.add_stage("Сделка", 1.0)

    lead = pipeline.create_lead("Иван Иванов", 50000, "email@example.com")
    lead.add_note("Позвонил, интересовался тарифом")
    lead.stage("Контакт")

    lead2 = pipeline.create_lead("Мария Петрова", 120000, "maria@mail.ru")
    lead2.add_note("Запросил демо-версию")
    lead2.stage("Демо")

    lead3 = pipeline.create_lead("Дмитрий Сидоров", 75000, "dima@corp.ru")
    lead3.stage("Прогноз")

    print(f"Активных лидов: {pipeline.active_count}")
    print(f"Сумма активных сделок: {pipeline.total_amount} руб.")
    print(f"Средний чек: {pipeline.average_amount:.2f} руб.")

    for lead in pipeline.leads:
        print(f"  - {lead.name} | Этап: {lead.current_stage} | Сумма: {lead.amount} руб.")

    pipeline.export_to_csv("sales_pipeline.csv")
    print("Данные экспортированы в sales_pipeline.csv")
