import psycopg2

con = psycopg2.connect(
    dbname='family_trees_db',
    user='postgres',
    password='1231',
    host='localhost',
    port='5432'
)

curs = con.cursor()

# Пробуем вставить наследуемый признак с несуществующим trait_id (например, 999)
try:
    curs.execute("""
        INSERT INTO inheritance (person_id, trait_id, value, notes)
        VALUES (1, 999, 'Test Value', 'Test note for non-existent trait');
    """)
    con.commit()
except Exception as e:
    print("Ошибка:", e, "Данного признака не существует в базе данных")

con.close()
