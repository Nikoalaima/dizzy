# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: SalesPipeline
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.role = "user" if "@" in email else "admin"

    @staticmethod
    def create(username, email):
        return User(username, email)


class ProfileManager:
    _profiles = {}
    _current_user = None

    @staticmethod
    def login(username, password=None):
        for u, p in ProfileManager._profiles.items():
            if p.username == username and (password is None or p.password == password):
                ProfileManager._current_user = u
                return True
        return False

    @staticmethod
    def logout():
        ProfileManager._current_user = None

    @staticmethod
    def get_current_user():
        return ProfileManager._current_user

    @staticmethod
    def add_profile(username, password="password", email=None):
        if username not in ProfileManager._profiles:
            user = User.create(username, email)
            ProfileManager._profiles[username] = (user, password)
            return True
        return False

    @staticmethod
    def list_profiles():
        return {u: p for u, p in ProfileManager._profiles.items()}
