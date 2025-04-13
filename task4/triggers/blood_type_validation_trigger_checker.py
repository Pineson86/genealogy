import psycopg2

con = psycopg2.connect(
    dbname='family_trees_db',
    user='postgres',
    password='1231',
    host='localhost',
    port='5432'
)

curs = con.cursor()

# Попробуем вставить недопустимое значение группы крови
try:
    curs.execute("""
        INSERT INTO inheritance (person_id, trait_id, value, notes)
        VALUES (1, 2, 'Z+', 'Ошибка');
    """)
    con.commit()
except Exception as e:
    print("Ошибка:", e, "Такой группы крови не существует")

con.close()
