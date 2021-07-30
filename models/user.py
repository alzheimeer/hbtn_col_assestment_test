from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Float, Integer, String, Boolean, DateTime
from config.db import meta, engine

users = Table("users", meta,
              Column("id", String(255), primary_key=True),  
              Column("name", String(50)),
              Column("lastname", String(50)),
              Column("gov_id", Integer),
              Column("email", String(80)),
              Column("company", String(50)),
              Column("password", String(255)),
              Column("active", Boolean) 
            )

meta.create_all(engine)
