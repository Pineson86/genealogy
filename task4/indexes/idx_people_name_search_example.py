import psycopg2

search_term = 'john'  # Ищем по имени

con = psycopg2.connect(
    dbname='family_trees_db',
    user='postgres',
    password='1231',
    host='localhost',
    port='5432'
)

curs = con.cursor()

curs.execute('''
    SELECT * FROM people
    WHERE LOWER(first_name) ILIKE %s;
''', (search_term + '%',))

results = curs.fetchall()
for person in results:
    print(person)

con.close()
