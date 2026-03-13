import sqlite3

conn = sqlite3.connect("internship.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")
cursor.execute("INSERT INTO interns VALUES (1,'Asha','Data Science',15000)")
cursor.execute("INSERT INTO interns VALUES (2,'Rahul','Web Development',12000)")
cursor.execute("INSERT INTO interns VALUES (3,'Sneha','Data Science',16000)")
cursor.execute("INSERT INTO interns VALUES (4,'Arjun','UI/UX',10000)")
cursor.execute("INSERT INTO interns VALUES (5,'Meera','Web Development',13000)")

conn.commit()
cursor.execute("SELECT name, track FROM interns")

rows = cursor.fetchall()

print("Intern Name and Track:")
for row in rows:
    print(row)
conn.close()