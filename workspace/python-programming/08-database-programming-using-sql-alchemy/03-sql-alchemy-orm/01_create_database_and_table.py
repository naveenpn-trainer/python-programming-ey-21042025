from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Book(Base):
    __tablename__ = "book_catalog"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    is_read = Column(Boolean)
    created_on = Column(Date)

#  Connecting to SQLite DB
# engine = create_engine("sqlite:///book_management_system.db")

#  Connecting to MySQL
engine = create_engine("mysql+mysqlconnector://root:qwerty@localhost/book_management_system")


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
