import psycopg2
import pandas as pd

#connect to postgresql
try:
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=Sutresnay2940")
    print("Connection Sucsess")
except:
    print("an exception occured")

#menampilkan hasil
#cur = conn.cursor()
#one = cur.fetchall()
#print(one)
#conn.commit()







