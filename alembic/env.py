from public.db import Base
from core.config import settings

from alembic import context

config = context.config

config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

target_metadata = Base.metadata
