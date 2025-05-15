from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, Date, insert
from datetime import date

engine = create_engine("sqlite:///book_management_system.db")
metadata = MetaData()
book_catalog = Table("book_catalog", metadata, autoload_with=engine)
with engine.connect() as con:
    statement = insert(book_catalog).values(name="Python Programming",
                                            author="Abhilash",
                                            is_read=False,
                                            created_on=date.today())
    con.execute(statement)
    con.commit()
