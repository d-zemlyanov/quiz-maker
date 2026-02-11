import os
from pathlib import Path

# Корневая директория проекта
BASE_DIR = Path(__file__).parent

# Директория для хранения данных
DATA_DIR = BASE_DIR / "data"

# Файлы данных
USERS_FILE = DATA_DIR / "users.json"
QUIZZES_FILE = DATA_DIR / "quizzes.json"
STATS_FILE = DATA_DIR / "statistics.json"

# Создаём папку data при импорте конфига
os.makedirs(DATA_DIR, exist_ok=True)