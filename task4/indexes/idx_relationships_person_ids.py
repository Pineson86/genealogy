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
    CREATE INDEX IF NOT EXISTS idx_relationships_person_ids
    ON relationships (person1_id, person2_id);
''')

con.commit()
con.close()
print("Индекс idx_relationships_person_ids создан.")
