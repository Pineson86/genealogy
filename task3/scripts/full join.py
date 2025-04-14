import psycopg2

# Подключение к базе данных
con = psycopg2.connect(
    dbname='family_trees_db',
    user='postgres',
    password='1231',
    host='localhost',
    port='5432'
)

curs = con.cursor()

# Выполнение запроса с FULL JOIN
curs.execute("""
    SELECT 
        people.first_name, 
        people.last_name, 
        traits.trait_name, 
        inheritance.value, 
        inheritance.notes
    FROM people
    FULL JOIN inheritance ON people.person_id = inheritance.person_id
    FULL JOIN traits ON inheritance.trait_id = traits.trait_id;
""")

# Получение и вывод результатов
results = curs.fetchall()
for row in results:
    first_name, last_name, trait_name, value, notes = row
    print(f"Имя: {first_name}, Фамилия: {last_name}, Признак: {trait_name}, Значение: {value}, Комментарий: {notes}")

# Закрытие соединения
con.close()
