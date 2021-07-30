from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Float, Integer, String, Boolean, DateTime
from config.db import meta, engine

payments = Table("payments", meta,
              Column("id", Integer, primary_key = True),
              Column("type", String(50)),
              Column("date", DateTime),
              Column("txn_id", Integer),
              Column("total", Float),
              Column("status", Boolean)
            )

meta.create_all(engine)