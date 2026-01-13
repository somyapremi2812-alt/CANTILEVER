🧾 Personal Finance Management System

A Python-based finance tracker that allows users to record and monitor their Income, Expenses, and Savings. The system stores data using SQLite, provides financial insights, and visualizes results through Matplotlib charts. A Tkinter GUI is optionally supported for a graphical interface.

🚀 Features

✔ Add & track Income
✔ Add & track Expenses
✔ Categorize transactions (Food, Rent, Salary, Travel, etc.)
✔ Calculate Total Income, Total Expenses, and Savings
✔ Persistent storage using SQLite Database
✔ Data visualization using Matplotlib (Bar Chart / Pie Chart)
✔ Optional Tkinter GUI

🛠️ Tech Stack
Component	Technology
Programming Language	Python
Database	SQLite
Visualization	Matplotlib
GUI (Optional)	Tkinter
📌 Project Flow

User inputs income/expense data

Data stored in SQLite database

Totals are calculated

Savings = Income − Expense

Data visualized via charts

🗄️ Database Schema

Table: finance

Column	Type	Details
id	INTEGER	Primary Key
type	TEXT	Income / Expense
category	TEXT	Category Name
amount	REAL	Money value
date	TEXT	Date (YYYY-MM-DD)
📁 Project Structure
📦 PersonalFinanceApp
 ┣ 📜 main.py
 ┣ 📜 db.py
 ┣ 📜 chart.py
 ┣ 📜 gui.py (optional)
 ┣ 📜 finance.db
 ┣ 📜 README.md
 ┗ 📜 requirements.txt

🧩 Example Code Snippet
def calculate_totals():
    cursor.execute("SELECT SUM(amount) FROM finance WHERE type='Income'")
    income = cursor.fetchone()[0] or 0
    
    cursor.execute("SELECT SUM(amount) FROM finance WHERE type='Expense'")
    expense = cursor.fetchone()[0] or 0

    savings = income - expense
    return income, expense, savings

📊 Visualization Example

The system generates a bar chart comparing:

Income

Expense

Savings

Using:

plt.bar(labels, values)
plt.title("Personal Finance Summary")
plt.show()

🔧 Installation & Setup
1. Clone the Repo
git clone https://github.com/YOUR-USERNAME/finance-manager.git
cd finance-manager

2. Install Dependencies
pip install -r requirements.txt

3. Run the Application
python main.py

📦 Dependencies

Include in requirements.txt

matplotlib
sqlite3 (bundled with Python)
tkinter (bundled in most environments)

🛠️ Future Enhancements

🔹 Login Authentication
🔹 Monthly Report Generation
🔹 Export to Excel / PDF
🔹 Budget Alerts
🔹 Cloud Sync

📚 Use Cases

✔ Students tracking expenses
✔ Freelancers tracking income/outflow
✔ Personal finance planning
✔ Budget monitoring

🧑‍💻 Author

your name
somya IT Maharaja agarsen institute of technology



