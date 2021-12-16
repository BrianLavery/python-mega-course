import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db") 
    cur = conn.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db") 
    cur = conn.cursor() 
    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("lite.db") 
    cur = conn.cursor() 
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db") 
    cur = conn.cursor() 
    cur.execute("DELETE FROM STORE WHERE item = ?", (item,)) # Need to add a comma here as only one parameter
    conn.commit()
    conn.close()

def update(item, quantity, price):
    conn = sqlite3.connect("lite.db") 
    cur = conn.cursor() 
    cur.execute("UPDATE store SET quantity = ?, price = ? WHERE item = ?", (quantity, price, item))
    conn.commit()
    conn.close()

print(view())
# delete("Coffee Cup")
update('Wine Glass', 16, 20)
print(view())
