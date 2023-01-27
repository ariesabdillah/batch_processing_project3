import psycopg2

conn = psycopg2.connect("host=localhost dbname=sekolah user=postgres password=Sutresnay2940")
cur = conn.cursor()

with open('C:/Users/abdil/OneDrive/Desktop/project/project3/source/latihan-database-table-guru.csv') as f:
    next(f)
    cur.copy_from(f,'guru', sep=';',columns=('id', 'name','phone', 'adress', 'mengajar'))
conn.commit