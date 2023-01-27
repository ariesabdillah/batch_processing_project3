import psycopg2
import csv
#connect to postgresql
conn = psycopg2.connect("host=localhost dbname=sekolah user=postgres password=Sutresnay2940")
cur = conn.cursor()

# insert data from csv to table
with open('C:/Users/abdil/OneDrive/Desktop/project/project3/source/latihan-database-table-guru.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader) #skip header
    for row in csv_reader:
        cur.execute("INSERT INTO guru VALUES(default, %s,%s,%s,%s,%s) ON CONFLICT DO NOTHING", row)
conn.commit()
