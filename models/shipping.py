from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Float, Integer, String, Boolean, DateTime
from config.db import meta, engine

shippings = Table("shippings", meta,
              Column("idShipping", Integer, primary_key = True),
              Column("address", String(60)),
              Column("city", String(60)),
              Column("state", String(60)),
              Column("country", String(60)),
              Column("cost", Float)
            )

meta.create_all(engine)