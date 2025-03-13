import psycopg2

con = psycopg2.connect(
    dbname='family_trees_db',
    user='postgres',
    password='1231',
    host='localhost',
    port='5432'
)

curs = con.cursor()

query = 'SELECT * FROM people;'  # Замените your_table_name на имя вашей таблицы
curs.execute(query)
results = curs.fetchall()
print(results)

con.close()
