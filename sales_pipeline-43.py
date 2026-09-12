# === Stage 43: Добавь пагинацию длинных списков ===
# Project: SalesPipeline
def paginate(items, page_size=10):
    total_pages = (len(items) + page_size - 1) // page_size
    pages = []
    for i in range(total_pages):
        start = i * page_size
        end = min(start + page_size, len(items))
        pages.append((start, end, items[start:end]))
    return pages, total_pages
