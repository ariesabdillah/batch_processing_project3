import pandas as pd
from sqlalchemy import create_engine
import os

file_path = r"/Users/abdil/OneDrive/Desktop/project/project3/source/project3-table siswa.csv"
file_name=os.path.basename(file_path).split(".")[0]

#cleansing email username
df = pd.read_csv(file_path, sep=';')
df['email'] = df['email'].apply(lambda x : x.split('@')[1])

#print(df['email'])
engine = create_engine('postgresql://postgres:Sutresnay2940@localhost:5432/postgres')
df.to_sql(file_name, engine)