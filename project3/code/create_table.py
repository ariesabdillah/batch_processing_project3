import psycopg2

#connect to postgresql
conn = psycopg2.connect("host=localhost dbname=sekolah user=postgres password=Sutresnay2940")
cur = conn.cursor()

#create table
#cur.execute("""
#            create table siswa(id serial PRIMARY KEY, email text, 
#            name text, phone text, postal_code text)
#"""
#)
cur.execute("""
           create table guru(id serial PRIMARY KEY, name text, 
            phone text, adress text, mengajar text)
"""
)
conn.commit()
print("Create Table Sucsess")