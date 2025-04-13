import psycopg2

person_id = 3  # Пример ID человека

con = psycopg2.connect(
    dbname='family_trees_db',
    user='postgres',
    password='1231',
    host='localhost',
    port='5432'
)

curs = con.cursor()

curs.execute('''
    SELECT * FROM relationships
    WHERE person1_id = %s OR person2_id = %s;
''', (person_id, person_id))

results = curs.fetchall()
for row in results:
    print(row)

con.close()
