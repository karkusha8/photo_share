from logging.config import fileConfig
import os

from sqlalchemy import create_engine
from sqlalchemy import pool

from alembic import context

from dotenv import load_dotenv

from app.database.db import Base
import app.models

# load .env
load_dotenv()

# this is the Alembic Config object
config = context.config

# logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# metadata
target_metadata = Base.metadata

# get database url from env
DATABASE_URL = os.getenv("DATABASE_URL")


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = create_engine(DATABASE_URL, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()