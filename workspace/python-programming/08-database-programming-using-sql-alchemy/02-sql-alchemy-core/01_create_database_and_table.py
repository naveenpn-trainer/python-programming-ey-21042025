from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, Date

# Create an engine
engine = create_engine("sqlite:///book_management_system.db")
metadata = MetaData()

#  Define a 'book_catalog' table
book_catalog = Table(
    "book_catalog", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String),
    Column("author", String),
    Column("is_read", Boolean),
    Column("created_on", Date)
)
#  Create table
metadata.create_all(engine)
