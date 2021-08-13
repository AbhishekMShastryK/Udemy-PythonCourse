import psycopg2

def create_table():
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'Abhi99' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Store (Item TEXT, Quantity INTEGER, Price REAL) ")
    conn.commit()
    conn.close()


def insert_data(Item,Quantity,Price):
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'Abhi99' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO Store VALUES (%s,%s,%s)",(Item,Quantity,Price))
    conn.commit()
    conn.close()

def view_data():
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'Abhi99' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_data(item):
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'Abhi99' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM Store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update_data(Quantity,Price,Item):
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'Abhi99' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("UPDATE Store SET Quantity=%s,price=%s WHERE Item=%s",(Quantity,Price,Item))
    conn.commit()
    conn.close()

create_table()
#update_data(12,250,'Apple')
insert_data('Orange',5,60)
#delete_data('Orange')
print(view_data())
