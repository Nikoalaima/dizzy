# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: SalesPipeline
def main_menu():
    print("\n=== Меню SalesPipeline ===")
    print("1. Добавить лида")
    print("2. Показать список лидов")
    print("3. Изменить статус/сумму/вероятность")
    print("4. Удалить лида")
    print("5. Вывести сводную статистику")
    print("6. Сохранить и выйти")
    try:
        choice = input("Выберите действие (1-6): ").strip()
        if choice == "1":
            add_lead()
        elif choice == "2":
            list_leads()
        elif choice == "3":
            edit_lead()
        elif choice == "4":
            delete_lead()
        elif choice == "5":
            show_stats()
        elif choice == "6":
            save_data()
            print("Данные сохранены. До свидания!")
            return True
    except KeyboardInterrupt:
        pass
    return False
