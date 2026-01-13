import sqlite3

conn = sqlite3.connect("finance.db", check_same_thread=False)
cursor = conn.cursor()

def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        category TEXT,
        amount REAL,
        date TEXT
    )
    """)
    conn.commit()

def add_transaction(t_type, category, amount, date):
    cursor.execute(
        "INSERT INTO transactions VALUES (NULL,?,?,?,?)",
        (t_type, category, amount, date)
    )
    conn.commit()

def fetch_transactions(month=None):
    if month:
        cursor.execute(
            "SELECT * FROM transactions WHERE date LIKE ?",
            (f"%-{month:02d}-%",)
        )
    else:
        cursor.execute("SELECT * FROM transactions")
    return cursor.fetchall()

def delete_transaction(transaction_id):
    cursor.execute(
        "DELETE FROM transactions WHERE id=?",
        (transaction_id,)
    )
    conn.commit()