import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db") # We are setting up a connection - it will create file if none exists
    cur = conn.cursor() # Set up cursor
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db") # We are setting up a connection - it will create file if none exists
    cur = conn.cursor() # Set up cursor
    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("lite.db") # We are setting up a connection - it will create file if none exists
    cur = conn.cursor() # Set up cursor
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

insert("Wine Glass", 8, 10)
print(view())