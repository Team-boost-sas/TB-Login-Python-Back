from sqlalchemy import create_engine, MetaData
from config.env import HOST_DB, DB_NAME, PASSWORD_DB, PORT_DB, USER_DB


connection_string = f"mysql+pymysql://{USER_DB}:{PASSWORD_DB}@{HOST_DB}:{PORT_DB}/{DB_NAME}"

engine = create_engine(connection_string, echo=True)

meta = MetaData()

conn = engine.connect()
