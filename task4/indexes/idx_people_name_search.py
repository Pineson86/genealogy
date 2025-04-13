import psycopg2

con = psycopg2.connect(
    dbname='family_trees_db',
    user='postgres',
    password='1231',
    host='localhost',
    port='5432'
)

curs = con.cursor()

curs.execute('''
    CREATE INDEX IF NOT EXISTS idx_people_name_search
    ON people (LOWER(first_name), LOWER(last_name), LOWER(middle_name));
''')

con.commit()
con.close()
print("Индекс idx_people_name_search создан.")
