from sqlalchemy import create_engine, delete, MetaData, Table

engine = create_engine("sqlite:///book_management_system.db")
metadata = MetaData()
book_catalog = Table("book_catalog", metadata, autoload_with=engine)
with engine.connect() as conn:
    statement = delete(book_catalog).where(book_catalog.c.name=="Python Programming")
    conn.execute(statement)
    conn.commit()