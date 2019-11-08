from psycopg_info import titanic_host, titanic_pass, titanic_user_db
import psycopg2
import pandas as pd

df = pd.read_csv('titanic.csv')

pg_conn = psycopg2.connect(dbname=titanic_user_db, user=titanic_user_db,
                           password=titanic_pass, host=titanic_host)
pg_curs = pg_conn.cursor()

create_titanic_table = '''
CREATE TABLE titanic (
    Survived INT,
    Pclass INT,
    Name TEXT,
    Sex TEXT,
    Age FLOAT,
    Siblings_Spouses_Aboard INT,
    Parents_Children_Aboard INT,
    Fare FLOAT
);
'''

pg_curs.execute(create_titanic_table)

titanic_list = []
for i in df.index:
    titanic_list.append(df.iloc[i, :].tolist())

for i in titanic_list:
    insert_titanic_data = '''
    INSERT INTO titanic
    (Survived, Pclass, Name, Sex, Age,
    Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
    VALUES''' + str(i).replace('[', '(').replace(']', ')') + ';'
    pg_curs.execute(insert_titanic_data)

pg_curs.close()
pg_conn.commit()