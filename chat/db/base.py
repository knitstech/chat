from sqlalchemy.orm import DeclarativeBase

from chat.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
