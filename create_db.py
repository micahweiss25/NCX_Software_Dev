import sqlite3


con = sqlite3.connect("tutorial.db")

cur = con.cursor()

cur.execute("CREATE TABLE USERS(name, phone_number)")

cur.execute("""
    INSERT INTO USERS VALUES
        ('John Doe', "555-555-5555"),
        ('Emily Smith', "555-555-5544")
""")

con.commit()
