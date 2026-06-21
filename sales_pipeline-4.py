# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: SalesPipeline
def edit_lead(lead_id: int, updates: dict) -> None:
    if lead_id not in leads:
        print(f"Лид с ID {lead_id} не найден.")
        return
    
    for key, value in updates.items():
        if hasattr(leads[lead_id], key):
            setattr(leads[lead_id], key, value)
        elif key in lead_notes and leads[lead_id].id == lead_id:
            lead_notes[key] = value

def delete_lead(lead_id: int) -> None:
    if lead_id not in leads:
        print(f"Лид с ID {lead_id} не найден.")
        return
    
    del leads[lead_id]
    for note_key, notes_list in list(lead_notes.items()):
        if any(note.get('id') == lead_id for note in notes_list):
            lead_notes[note_key].remove(next(n for n in notes_list if n.get('id') == lead_id))
