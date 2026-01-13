import sqlite3
import matplotlib.pyplot as plt

def show_summary():
    conn = sqlite3.connect("finance.db")
    cur = conn.cursor()

    cur.execute("SELECT type, SUM(amount) FROM transactions GROUP BY type")
    data = cur.fetchall()
    conn.close()

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    plt.bar(labels, values)
    plt.title("Income vs Expenses")
    plt.ylabel("Amount")
    plt.show()