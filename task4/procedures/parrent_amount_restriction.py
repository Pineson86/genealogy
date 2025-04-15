import psycopg2

def insert_parent_relationship(cursor, parent_id, child_id, start_date=None, end_date=None):
    cursor.execute("""
        SELECT COUNT(*) FROM relationships
        WHERE person2_id = %s AND relationship_type = 'родитель-ребенок';
    """, (child_id,))
    parent_count = cursor.fetchone()[0]

    if parent_count >= 2:
        raise Exception("У ребёнка уже два родителя.")

    cursor.execute("""
        INSERT INTO relationships (person1_id, person2_id, relationship_type, start_date, end_date)
        VALUES (%s, %s, 'родитель-ребенок', %s, %s);
    """, (parent_id, child_id, start_date, end_date))

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
    # Допустим, у Olivia (id=10) уже есть два родителя — добавим третьего
    insert_parent_relationship(curs, 5, 10)
    con.commit()
    print("Родительская связь успешно добавлена.")
except Exception as e:
    con.rollback()
    print("Ошибка:", e)

curs.close()
con.close()
