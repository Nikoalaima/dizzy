# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: SalesPipeline
APP_CONFIG = {
    "app_name": "SalesPipeline",
    "version": "1.0",
    "default_lead_value": 10_000,
    "probability_steps": [10, 25, 40, 60, 75],
    "stage_names": ["Lead", "Contacted", "Qualified", "Proposal", "Negotiation", "Closed"],
    "currency_symbol": "$",
    "max_notes_per_lead": 10,
    "notification_enabled": True,
    "log_level": "INFO",
}


def get_config(key: str = None):
    if key is None:
        return APP_CONFIG.copy()
    return APP_CONFIG.get(key)


def print_app_info():
    print(f"App: {APP_CONFIG['app_name']} v{APP_CONFIG['version']}, "
          f"Currency: {APP_CONFIG['currency_symbol']}, "
          f"Stages: {len(APP_CONFIG['stage_names'])}")
