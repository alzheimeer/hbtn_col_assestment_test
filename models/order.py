from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Float, Integer, String, Boolean, DateTime
from config.db import meta, engine

orders = Table("orders", meta,
              Column("idOrder", Integer, primary_key = True),
              Column("date", DateTime),
              Column("total", Float),
              Column("subtotal", Float),
              Column("taxes", Float),
              Column("paid", Float)
            )

meta.create_all(engine)