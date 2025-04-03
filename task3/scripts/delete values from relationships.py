import psycopg2

con = psycopg2.connect(
    dbname='family_trees_db',
    user='postgres',
    password='1231',
    host='localhost',
    port='5432'
)

curs = con.cursor()

# Удаление связи между двумя людьми
person1_id = 1
person2_id = 2

curs.execute(
    "DELETE FROM relationships WHERE person1_id = %s AND person2_id = %s OR person1_id = %s AND person2_id = %s;",
    (person1_id, person2_id, person2_id, person1_id)
)
con.commit()

con.close()
print(f'Relationship between person {person1_id} and person {person2_id} deleted')
