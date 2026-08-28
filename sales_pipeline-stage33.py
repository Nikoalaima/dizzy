# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: SalesPipeline
def undo():
    """Откат последнего действия в SalesPipeline."""
    if not _undo_stack:
        print("Нет действий для отката.")
        return
    last = _undo_stack.pop()
    print(f"Откат: {last}")
