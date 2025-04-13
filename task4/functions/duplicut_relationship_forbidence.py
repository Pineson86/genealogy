import psycopg2

def insert_relationship_no_duplicates(cursor, person1_id, person2_id, relationship_type, start_date=None, end_date=None):
    cursor.execute("""
        SELECT COUNT(*) FROM relationships
        WHERE person1_id = %s AND person2_id = %s AND relationship_type = %s;
    """, (person1_id, person2_id, relationship_type))
    count = cursor.fetchone()[0]

    if count > 0:
        raise Exception("Такая связь уже существует.")

    cursor.execute("""
        INSERT INTO relationships (person1_id, person2_id, relationship_type, start_date, end_date)
        VALUES (%s, %s, %s, %s, %s);
    """, (person1_id, person2_id, relationship_type, start_date, end_date))

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
    # Попытка добавить уже существующую связь (будет ошибка)
    insert_relationship_no_duplicates(curs, 1, 2, 'супруг')
    con.commit()
    print("Связь успешно добавлена.")
except Exception as e:
    con.rollback()
    print("Ошибка:", e)

curs.close()
con.close()
