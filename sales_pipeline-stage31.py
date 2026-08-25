# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: SalesPipeline
def switch_profile(self, profile_id):
        """Переключить активный пользовательский профиль."""
        profiles = self._get_profiles()
        if profile_id not in profiles:
            raise ValueError(f"Профиль '{profile_id}' не найден")
        self._active_profile_id = profile_id
        return self._get_profiles()[profile_id]
