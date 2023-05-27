from sqlalchemy import Column, Table, Index, DateTime, Boolean
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func

from config.db import meta, engine

users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True),
    Column("email", String(255), index=True),
    Column("password", String(255)),
    Column("phone", String(255)),
    Column("secret", String(255), default=""),
    Column("updated_at", DateTime, server_default=func.now()),
    Column("created_at", DateTime, server_default=func.now()),
    Column("status", String(255), default="created"),
    Column("status_email", Boolean, default=False),
    Column("status_phone", Boolean, default=False),
)

index_email = Index('idx_email', users.c.email)
index_email.create(bind=engine)

meta.create_all(engine)
