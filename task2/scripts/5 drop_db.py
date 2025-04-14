import psycopg2

db_name_to_drop = 'family_trees_db'

con = None  # Инициализируем con вне блока try

try:
    con = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='1231',
        host='localhost'
    )

    con.autocommit = True

    with con.cursor() as curs:
        # Перед удалением базы данных необходимо отключить от нее все соединения.
        # Простейший способ - принудительно завершить все сеансы, подключенные к базе данных.
        curs.execute(f"""
            SELECT pg_terminate_backend(pg_stat_activity.pid)
            FROM pg_stat_activity
            WHERE pg_stat_activity.datname = '{db_name_to_drop}'
              AND pg_stat_activity.pid <> pg_backend_pid();
        """)
        print(f"Отключены все сеансы, подключенные к базе данных '{db_name_to_drop}'.")

        # Теперь можно удалить базу данных
        curs.execute(f'DROP DATABASE IF EXISTS {db_name_to_drop};')
        print(f"База данных '{db_name_to_drop}' успешно удалена.")

except psycopg2.Error as e:
    print(f"Ошибка при удалении базы данных: {e}")

finally:
    if con:
        con.close()
        print("Соединение с PostgreSQL закрыто.")