import sqlite3
import getpass
import datetime

# Database setup
def setup_database():
    conn = sqlite3.connect('finance_tracker.db')
    c = conn.cursor()
    
    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY,
                 username TEXT NOT NULL UNIQUE,
                 password TEXT NOT NULL)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                 id INTEGER PRIMARY KEY,
                 user_id INTEGER,
                 amount REAL,
                 category TEXT,
                 type TEXT,
                 date TEXT,
                 FOREIGN KEY(user_id) REFERENCES users(id))''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS budgets (
                 id INTEGER PRIMARY KEY,
                 user_id INTEGER,
                 category TEXT,
                 amount REAL,
                 FOREIGN KEY(user_id) REFERENCES users(id))''')
    
    conn.commit()
    conn.close()

# User authentication
def register_user():
    conn = sqlite3.connect('finance_tracker.db')
    c = conn.cursor()
    
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
    
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    
    conn.close()

def login_user():
    conn = sqlite3.connect('finance_tracker.db')
    c = conn.cursor()
    
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    
    c.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    
    if user:
        print("Login successful.")
        return user[0]
    else:
        print("Invalid credentials.")
        return None
    
    conn.close()

# Transaction logging
def add_transaction(user_id):
    conn = sqlite3.connect('finance_tracker.db')
    c = conn.cursor()
    
    amount = float(input("Enter the amount: "))
    category = input("Enter the category: ")
    type = input("Enter the type (Income/Expense): ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    c.execute("INSERT INTO transactions (user_id, amount, category, type, date) VALUES (?, ?, ?, ?, ?)",
              (user_id, amount, category, type, date))
    conn.commit()
    conn.close()
    print("Transaction added successfully.")

# Budget management
def set_budget(user_id):
    conn = sqlite3.connect('finance_tracker.db')
    c = conn.cursor()
    
    category = input("Enter the category: ")
    amount = float(input("Enter the budget amount: "))
    
    c.execute("INSERT INTO budgets (user_id, category, amount) VALUES (?, ?, ?)",
              (user_id, category, amount))
    conn.commit()
    conn.close()
    print("Budget set successfully.")

# Report generation
def generate_report(user_id):
    conn = sqlite3.connect('finance_tracker.db')
    c = conn.cursor()
    
    c.execute("SELECT category, SUM(amount) FROM transactions WHERE user_id = ? AND date >= datetime('now', 'start of month') AND type = 'Expense' GROUP BY category", (user_id,))
    expenses = c.fetchall()
    
    print("\nMonthly Expense Report:")
    total_expenses = 0
    for category, amount in expenses:
        print(f"{category}: ${amount:.2f}")
        total_expenses += amount
    print(f"Total Expenses: ${total_expenses:.2f}\n")
    
    c.execute("SELECT category, amount FROM budgets WHERE user_id = ?", (user_id,))
    budgets = c.fetchall()
    
    print("Budget Insights:")
    for category, budget in budgets:
        c.execute("SELECT SUM(amount) FROM transactions WHERE user_id = ? AND category = ? AND date >= datetime('now', 'start of month') AND type = 'Expense'", (user_id, category))
        spent = c.fetchone()[0]
        if spent:
            print(f"{category}: Budget - ${budget:.2f}, Spent - ${spent:.2f}, Remaining - ${budget - spent:.2f}")
        else:
            print(f"{category}: Budget - ${budget:.2f}, Spent - $0.00, Remaining - ${budget:.2f}")
    
    conn.close()

# Main application loop
def main():
    setup_database()
    
    print("Welcome to Personal Finance Tracker!")
    print("1. Register")
    print("2. Login")
    choice = input("Choose an option: ")
    
    if choice == '1':
        register_user()
    elif choice == '2':
        user_id = login_user()
        if user_id:
            while True:
                print("\n1. Add Transaction")
                print("\n2. Set Budget")
                print("\n3. Generate Report")
                print("\n4. Logout")
                choice = input("Choose an option: ")
                
                if choice == '1':
                    add_transaction(user_id)
                elif choice == '2':
                    set_budget(user_id)
                elif choice == '3':
                    generate_report(user_id)
                elif choice == '4':
                    break
                else:
                    print("Invalid choice. Please try again.")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
