from sqlalchemy import create_engine, update, MetaData, Table

engine = create_engine("sqlite:///book_management_system.db")
metadata = MetaData()
book_catalog = Table("book_catalog", metadata, autoload_with=engine)
with engine.connect() as conn:
    statement = update(book_catalog).where(book_catalog.c.name == "Python Programming").values(is_read=True)
    conn.execute(statement)
    conn.commit()