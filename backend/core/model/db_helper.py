from backend.core.config import settings


class DatabaseHelper:
    pass

db_helper = DatabaseHelper(
    url = settings.db_url,
    echo = settings.db_echo,
)