import customtkinter as ctk
from tkinter import ttk, messagebox
from datetime import date
import matplotlib.pyplot as plt
import database

# ---------------- CONFIG ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

database.create_table()

app = ctk.CTk()
app.geometry("1100x650")
app.title("Personal Finance Manager")

selected_month = ctk.IntVar(value=0)

# ---------------- FUNCTIONS ----------------
def refresh_table():
    for row in tree.get_children():
        tree.delete(row)

    data = database.fetch_transactions(
        selected_month.get() if selected_month.get() else None
    )

    for r in data:
        tree.insert("", "end", values=r)

def add_transaction(t_type):
    if not category.get() or not amount.get():
        return

    database.add_transaction(
        t_type,
        category.get(),
        float(amount.get()),
        date.today()
    )

    category.delete(0, "end")
    amount.delete(0, "end")
    refresh_table()

def delete_selected():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Select a transaction")
        return

    transaction_id = tree.item(selected[0])["values"][0]
    database.delete_transaction(transaction_id)
    refresh_table()

# ---------------- ANALYTICS WINDOW ----------------
def open_analytics():
    data = database.fetch_transactions()

    income = sum(x[3] for x in data if x[1] == "Income")
    expense = sum(x[3] for x in data if x[1] == "Expense")

    # -------- PIE CHART --------
    plt.figure(figsize=(5,5))
    plt.pie(
        [income, expense],
        labels=["Income", "Expense"],
        autopct="%1.1f%%",
        startangle=140
    )
    plt.title("Income vs Expense")
    plt.show()

    # -------- MONTHLY EXPENSE BAR GRAPH --------
    monthly = [0]*12
    for t in data:
        if t[1] == "Expense":
            month = int(t[4].split("-")[1])
            monthly[month-1] += t[3]

    plt.figure(figsize=(8,4))
    plt.bar(
        ["Jan","Feb","Mar","Apr","May","Jun",
         "Jul","Aug","Sep","Oct","Nov","Dec"],
        monthly
    )
    plt.title("Monthly Expenses")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.show()

# ---------------- TITLE ----------------
ctk.CTkLabel(
    app,
    text="💰 Personal Finance Manager",
    font=("Segoe UI", 22, "bold")
).pack(pady=15)

# ---------------- INPUT BAR ----------------
input_frame = ctk.CTkFrame(app)
input_frame.pack(pady=10)

category = ctk.CTkEntry(input_frame, placeholder_text="Category", width=180)
category.pack(side="left", padx=6)

amount = ctk.CTkEntry(input_frame, placeholder_text="Amount", width=180)
amount.pack(side="left", padx=6)

ctk.CTkButton(
    input_frame,
    text="Add Income",
    fg_color="#22c55e",
    command=lambda: add_transaction("Income")
).pack(side="left", padx=6)

ctk.CTkButton(
    input_frame,
    text="Add Expense",
    fg_color="#ef4444",
    command=lambda: add_transaction("Expense")
).pack(side="left", padx=6)

ctk.CTkButton(
    input_frame,
    text="Delete",
    fg_color="#dc2626",
    command=delete_selected
).pack(side="left", padx=6)

ctk.CTkButton(
    input_frame,
    text="Analytics",
    fg_color="#6366f1",
    command=open_analytics
).pack(side="left", padx=6)

# ---------------- MONTH FILTER ----------------
ctk.CTkOptionMenu(
    app,
    values=["All","01","02","03","04","05","06","07","08","09","10","11","12"],
    command=lambda m: (
        selected_month.set(int(m)) if m != "All" else selected_month.set(0),
        refresh_table()
    )
).pack(pady=10)

# ---------------- TREEVIEW DARK THEME ----------------
style = ttk.Style()
style.theme_use("default")

style.configure(
    "Treeview",
    background="#1e1e1e",
    foreground="white",
    fieldbackground="#1e1e1e",
    rowheight=30
)

style.configure(
    "Treeview.Heading",
    background="#111111",
    foreground="white"
)

style.map(
    "Treeview",
    background=[("selected", "#2563eb")]
)

# ---------------- TABLE ----------------
tree = ttk.Treeview(
    app,
    columns=("ID","Type","Category","Amount","Date"),
    show="headings"
)

for col in ("ID","Type","Category","Amount","Date"):
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.column("ID", width=60)
tree.pack(fill="both", expand=True, padx=20, pady=15)

# ---------------- START ----------------
refresh_table()
app.mainloop()