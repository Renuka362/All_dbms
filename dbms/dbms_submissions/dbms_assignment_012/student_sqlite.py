import sqlite3

conn = sqlite3.connect('Student.sqlite3')
c = conn.cursor()
c.execute("""CREATE TABLE Student (name text,age integer,score float,student_id integer)""")
c.execute("INSERT INTO Student VALUES ('Renuka',23,95,362)")
c.execute("SELECT * FROM Student WHERE age = 23")
conn.commit()
conn.close()