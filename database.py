from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import pyodbc

username = 'sa'
password = 'bySqlServer2020'
server = 'localhost'
port = '1433'
database='master'



SQLALCHEMY_DATABASE_URL = (
    f"mssql+pyodbc://{username}:{password}@{server}:{port}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
)

#database_url = f"mssql+pymssql://{username}:{password}@{server}:{port}/{database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL,pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

