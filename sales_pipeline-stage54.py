# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: SalesPipeline
import json, os

def load_favorites():
    path = os.path.join(os.path.dirname(__file__), "favorites.json")
    if os.path.exists(path):
        try:
            return json.load(open(path, encoding="utf-8"))
        except Exception:
            return []
    return []

def save_favorites(items):
    path = os.path.join(os.path.dirname(__file__), "favorites.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

FAVORITES = load_favorites()

def is_favorite(item_id):
    return item_id in FAVORITES

def toggle_favorite(item_id):
    if item_id in FAVORITES:
        FAVORITES.remove(item_id)
    else:
        FAVORITES.append(item_id)
    save_favorites(FAVORITES)
    return FAVORITES

def quick_access():
    return [item for item in ALL_LEADS if item["id"] in FAVORITES]
