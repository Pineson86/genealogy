import psycopg2

con = psycopg2.connect(
    dbname='family_trees_db',
    user='postgres',
    password='1231',
    host='localhost',
    port='5432'
)

curs = con.cursor()

try:
    curs.execute("""
    INSERT INTO people (
        first_name, middle_name, last_name, birth_date, birth_place, death_date, death_place, gender, bio
    ) VALUES (
        'Test', NULL, 'Futureman', '2050-01-01', 'Nowhere', NULL, NULL, 'мужской', 'invalid birth'
    );
    """)
    con.commit()
except Exception as e:
    print("Ошибка:", e)

con.close()
