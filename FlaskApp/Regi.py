import psycopg2

con = psycopg2.connect(
  database="postgres",
  user="postgres",
  password="Qazwsxedc",
  host="127.0.0.1",
  port="5432"
)


cur = con.cursor()
cur.execute('''CREATE TABLE STUDENT 
    (Mail TEXT PRIMARY KEY NOT NULL, 
    Power INT NOT NULL);''')
con.commit()
con.close()