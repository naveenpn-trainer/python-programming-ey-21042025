from sqlalchemy import create_engine, select, MetaData, Table

engine = create_engine("sqlite:///book_management_system.db")
metadata = MetaData()
book_catalog = Table("book_catalog", metadata, autoload_with=engine)
with engine.connect() as conn:
    statement = select(book_catalog)
    result = conn.execute(statement)
    for record in result:
        print(record)
        print(record.created_on)
