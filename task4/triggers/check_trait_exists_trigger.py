import psycopg2

con = psycopg2.connect(
    dbname='family_trees_db',
    user='postgres',
    password='1231',
    host='localhost',
    port='5432'
)

curs = con.cursor()

# Удалим триггер и функцию, если уже существуют
curs.execute("DROP TRIGGER IF EXISTS check_trait_exists_trigger ON inheritance;")
curs.execute("DROP FUNCTION IF EXISTS check_trait_exists();")

# Создание функции
curs.execute("""
CREATE OR REPLACE FUNCTION check_trait_exists()
RETURNS TRIGGER AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM traits WHERE trait_id = NEW.trait_id
    ) THEN
        RAISE EXCEPTION 'Указанный признак не существует.';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
""")

# Создание триггера
curs.execute("""
CREATE TRIGGER check_trait_exists_trigger
BEFORE INSERT ON inheritance
FOR EACH ROW
EXECUTE FUNCTION check_trait_exists();
""")

con.commit()
con.close()

print("check_trait_exists_trigger создан.")
