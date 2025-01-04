import sqlite3

class MetadataStore:
    def __init__(self, db_path='metadata.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS metadata (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    description TEXT,
                    additional_info TEXT
                )
            """)

    def add_metadata(self, title, description, additional_info):
        with self.conn:
            self.conn.execute("""
                INSERT INTO metadata (title, description, additional_info)
                VALUES (?, ?, ?)
            """, (title, description, additional_info))

    def query_metadata(self, title):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM metadata WHERE title LIKE ?
        """, (f"%{title}%",))
        return cursor.fetchall()