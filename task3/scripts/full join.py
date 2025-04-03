import psycopg2

con = psycopg2.connect(
    dbname='family_trees_db',
    user='postgres',
    password='1231',
    host='localhost',
    port='5432'
)

curs = con.cursor()


curs.execute("""
    SELECT people.first_name, people.last_name, traits.trait_name
    FROM people
    FULL JOIN inheritance ON people.person_id = inheritance.person_id
    FULL JOIN traits ON inheritance.trait_id = traits.trait_id;
""")

results = curs.fetchall()
for row in results:
    print(row)
