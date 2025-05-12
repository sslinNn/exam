import asyncio
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine

from config import DB_URL

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
from src.models import Base

# Используем метаданные из единого Base
target_metadata = Base.metadata

# Создаём асинхронный движок
connectable = create_async_engine(DB_URL, echo=True)

async def run_migrations_online():
    """Запуск миграций в режиме online."""
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

def do_run_migrations(connection):
    """Настройка и выполнение миграций."""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,  # Сравнивать типы данных
        compare_server_default=True,  # Сравнивать значения по умолчанию на сервере
    )
    with context.begin_transaction():
        context.run_migrations()

if context.is_offline_mode():
    raise RuntimeError("Offline migrations are not supported.")
else:
    asyncio.run(run_migrations_online())