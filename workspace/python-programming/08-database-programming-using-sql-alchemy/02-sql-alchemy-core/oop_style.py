from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, Date, insert, select
from datetime import date

class BookManager:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.metadata = MetaData()
        self.book_catalog = Table(
            "book_catalog", self.metadata,
            Column("id", Integer, primary_key=True, autoincrement=True),
            Column("name", String),
            Column("author", String),
            Column("is_read", Boolean),
            Column("created_on", Date)
        )
        self.metadata.create_all(self.engine)

    def add_books(self, name, author):
        with self.engine.connect() as con:
            statement = insert(self.book_catalog).values(name="Python Programming",
                                                    author="Abhilash",
                                                    is_read=False,
                                                    created_on=date.today())
            con.execute(statement)
            con.commit()

    def list_books(self):
        with self.engine.connect() as conn:
            statement = select(self.book_catalog)
            result = conn.execute(statement)
            for record in result:
                print(record)
                print(record.created_on)

if __name__ == '__main__':
    book_manager = BookManager(db_url="sqlite:///book_management_system.db")
    book_manager.add_books("Python Programming", "Abhilash")
    book_manager.list_books()