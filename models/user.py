from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

users = Table("users", meta,
              Column("id", Integer, primary_key = True),
              Column("name", String(255)),
              Column("lastname", String(255)),
              Column("gov_id", Integer),
              Column("email", String(255)),
              Column("company", String(255)),
              Column("password", String(255))
            )

meta.create_all(engine)