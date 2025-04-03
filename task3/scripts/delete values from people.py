import psycopg2

con = psycopg2.connect(
    dbname='family_trees_db',
    user='postgres',
    password='1231',
    host='localhost',
    port='5432'
)

curs = con.cursor()

# Удаление человека по имени
name_to_delete = 'John'
curs.execute("DELETE FROM people WHERE first_name = %s;", (name_to_delete,))
con.commit()

con.close()
print(f'Person with name {name_to_delete} deleted')
