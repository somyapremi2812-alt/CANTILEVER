from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("contacts.db")

# Create table
with get_db() as db:
    db.execute("""
    CREATE TABLE IF NOT EXISTS contacts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        email TEXT
    )
    """)

@app.route("/")
def index():
    db = get_db()
    contacts = db.execute("SELECT * FROM contacts").fetchall()
    return render_template("index.html", contacts=contacts)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]

        db = get_db()
        db.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
                   (name, phone, email))
        db.commit()
        return redirect("/")
    return render_template("add.html")

@app.route("/delete/<int:id>")
def delete(id):
    db = get_db()
    db.execute("DELETE FROM contacts WHERE id=?", (id,))
    db.commit()
    return redirect("/")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    db = get_db()
    contact = db.execute("SELECT * FROM contacts WHERE id=?", (id,)).fetchone()

    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]

        db.execute("UPDATE contacts SET name=?, phone=?, email=? WHERE id=?",
                   (name, phone, email, id))
        db.commit()
        return redirect("/")

    return render_template("edit.html", contact=contact)

if __name__ == "__main__":
    app.run(debug=True)
