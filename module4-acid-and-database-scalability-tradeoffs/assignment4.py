import os
import psycopg2

conn = psycopg2.connect(dbname=os.getenv('TITANIC_USER_DB'),
                        user=os.getenv('TITANIC_USER_DB'),
                        password=os.getenv('TITANIC_PASS'),
                        host=os.getenv('TITANIC_HOST'))
curs = conn.cursor()

curs.execute('''SELECT COUNT(*)
                FROM titanic
                WHERE survived = 0;
                ''')
print('Died: ', c.fetchall())

curs.execute('''SELECT COUNT(*)
                FROM titanic
                WHERE survived = 1;
                ''')
print('Survived: ', c.fetchall())

curs.execute('SELECT pclass, COUNT(*) FROM titanic \
              GROUP BY pclass \
              ORDER BY pclass;')

pass_class = curs.fetchall()

for i in range(len(pass_class)):
    print(f'Class {pass_class[i][0]} had {pass_class[i][1]} passengers')


curs.execute('SELECT pclass, COUNT(*) FROM titanic\
              WHERE survived = 0\
              GROUP BY pclass\
              ORDER BY pclass;')

dead_class = curs.fetchall()

for i in range(len(dead_class)):
    print(f'Class {dead_class[i][0]} had {dead_class[i][1]} passengers who died')

curs.execute('SELECT pclass, COUNT(*) FROM titanic\
              WHERE survived = 1\
              GROUP BY pclass\
              ORDER BY pclass;')

live_class = curs.fetchall()

for i in range(len(live_class)):
    print(f'Class {live_class[i][0]} had {live_class[i][1]} passengers who lived')

curs.execute('SELECT survived, AVG(age) FROM titanic\
              GROUP BY survived;')

avg_age = curs.fetchall()

print(f'Average survivor age: {avg_age[1][1]:.02f} years old')
print(f'Average non-survivors age: {avg_age[0][1]:.02f} years old')

curs.execute('SELECT pclass, AVG(age) FROM titanic\
              GROUP BY pclass\
              ORDER BY pclass;')

avg_age_class = curs.fetchall()

for i in range(len(avg_age_class)):
    print(f'Class {i+1} average age: {avg_age_class[i][1]:.02f}')

curs.execute('SELECT pclass, AVG(fare) FROM titanic\
              GROUP BY pclass\
              ORDER BY pclass;')

avg_fare_class = curs.fetchall()

for i in range(len(avg_fare_class)):
    print(f'Class {i+1} average fare: ${avg_fare_class[i][1]:.02f}')

curs.execute('SELECT survived, AVG(fare) FROM titanic\
              GROUP BY survived\
              ORDER BY survived;')

avg_fare_survived = curs.fetchall()

print(f'Survivor average fare: ${avg_fare_survived[1][1]:.02f}')
print(f'Non-Survivor average fare: ${avg_fare_survived[0][1]:.02f}')

curs.execute('SELECT pclass, AVG(siblings_spouses_aboard) FROM titanic\
              GROUP BY pclass\
              ORDER BY pclass;')

sib_avg_class = curs.fetchall()

for i in range(len(sib_avg_class)):
    print(f'Class {sib_avg_class[i][0]} averaged {float(sib_avg_class[i][1]):.02f} siblings or spouses')

curs.execute('SELECT survived, AVG(siblings_spouses_aboard) FROM titanic\
              GROUP BY survived\
              ORDER BY survived;')

sib_avg_surv = curs.fetchall()

print(f'Survivors averaged {float(sib_avg_surv[1][1]):.02f} siblings or spouses')
print(f'Non-Survivors averaged {float(sib_avg_surv[0][1]):.02f} siblings or spouses')

curs.execute('SELECT pclass, AVG(parents_children_aboard) FROM titanic\
              GROUP BY pclass\
              ORDER BY pclass;')

par_avg_class = curs.fetchall()

for i in range(len(par_avg_class)):
    print(f'Class {par_avg_class[i][0]} averaged {float(par_avg_class[i][1]):.02f} parents or children')

curs.execute('SELECT survived, AVG(parents_children_aboard) FROM titanic\
              GROUP BY survived\
              ORDER BY survived;')

par_avg_surv = curs.fetchall()

print(f'Survivors averaged {float(par_avg_surv[1][1]):.02f} parents or children')
print(f'Non-Survivors averaged {float(par_avg_surv[0][1]):.02f} parents or children')

curs.execute('SELECT COUNT(DISTINCT name) FROM titanic;')
distinct_names = curs.fetchall()

curs.execute('SELECT COUNT(name) FROM titanic;')
all_names = curs.fetchall()

distinct_names == all_names