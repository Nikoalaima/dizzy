# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: SalesPipeline
def add_tag(self, lead_id: int, tag: str) -> None:
    if self.tags is None:
        self.tags = {}
    tags_list = self.tags.get(lead_id, [])
    if tag not in tags_list:
        tags_list.append(tag)
        self.tags[lead_id] = tags_list

def remove_tag(self, lead_id: int, tag: str) -> bool:
    if self.tags is None or lead_id not in self.tags:
        return False
    tags_list = self.tags.get(lead_id, [])
    if tag in tags_list:
        tags_list.remove(tag)
        if not tags_list:
            del self.tags[lead_id]
        else:
            self.tags[lead_id] = tags_list
        return True
    return False
