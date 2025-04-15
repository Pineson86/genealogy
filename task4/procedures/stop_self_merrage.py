import psycopg2

def insert_spouse_relationship(cursor, person1_id, person2_id, start_date=None, end_date=None):
    if person1_id == person2_id:
        raise Exception("Нельзя вступать в брак с самим собой.")

    cursor.execute("""
        INSERT INTO relationships (person1_id, person2_id, relationship_type, start_date, end_date)
        VALUES (%s, %s, 'супруг', %s, %s);
    """, (person1_id, person2_id, start_date, end_date))

# --- Запуск ---
con = psycopg2.connect(
    dbname='family_trees_db',
    user='postgres',
    password='1231',
    host='localhost',
    port='5432'
)
curs = con.cursor()

try:
    # Попытка добавить "сам на себе"
    insert_spouse_relationship(curs, 4, 4)
    con.commit()
    print("Брак успешно добавлен.")
except Exception as e:
    con.rollback()
    print("Ошибка:", e)

curs.close()
con.close()
