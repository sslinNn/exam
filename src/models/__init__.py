from sqlalchemy.ext.declarative import declarative_base

# Создаем единый Base для всех моделей
Base = declarative_base()

# Импортируем все модели после создания Base
from .partners import *  # noqa 