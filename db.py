import sqlite3

database = "student.db"

def create_tables():
    conn  = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NNULL, 
        )
    """)
    conn.commit()
    cursor.close()
    print("✅ Database and table created successfully!")


def insert_sample_data():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    sample_data = [
        ("What is Python?", "Python is a high-level programming language."),
        ("What is LangChain?", "LangChain is a framework for building applications with LLMs."),
        ("What is SQLite?", "SQLite is a lightweight, file-based database.")
    ]

    cursor.executemany("INSERT INTO database (question, answer) VALUES (?, ?)", sample_data)
    conn.commit()
    cursor.close()
    print("Sample data inserted")

if __name__ == "__main__":
    create_tables()
    insert_sample_data()