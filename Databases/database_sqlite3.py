import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Store (Item TEXT, Quantity INTEGER, Price REAL) ")
    conn.commit()
    conn.close()


def insert_data(Item,Quantity,Price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Store VALUES (?,?,?)",(Item,Quantity,Price))
    conn.commit()
    conn.close()

def view_data():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_data(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM Store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update_data(Quantity,Price,Item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE Store SET Quantity=?,price=? WHERE Item=?",(Quantity,Price,Item))
    conn.commit()
    conn.close()

create_table()
#update_data(12,250,'Apple')
insert_data('Orange',5,50)
#delete_data('Orange')
print(view_data())
