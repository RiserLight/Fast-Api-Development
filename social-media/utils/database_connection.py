
import psycopg2
from psycopg2.extras import RealDictCursor
import logging



async def get_db():
  try:
    conn=await psycopg2.connect(host='localhost',database='social-media-app',user='Postgres',password='Mysql',cursor_factory=RealDictCursor)
    cursor=conn.cursor()
    logging.info("Connection to database successfull")
  except Exception as e:
    raise e


