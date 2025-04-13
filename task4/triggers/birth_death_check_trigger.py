import psycopg2

con = psycopg2.connect(
    dbname='family_trees_db',
    user='postgres',
    password='1231',
    host='localhost',
    port='5432'
)

curs = con.cursor()

# Удалим на всякий случай, если уже есть
curs.execute("DROP TRIGGER IF EXISTS birth_death_check_trigger ON people;")
curs.execute("DROP FUNCTION IF EXISTS check_birth_death_dates();")

# Создание функции
curs.execute("""
CREATE OR REPLACE FUNCTION check_birth_death_dates()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.birth_date > CURRENT_DATE THEN
        RAISE EXCEPTION 'Дата рождения не может быть в будущем.';
    END IF;
    IF NEW.death_date IS NOT NULL AND NEW.birth_date > NEW.death_date THEN
        RAISE EXCEPTION 'Дата смерти не может быть раньше даты рождения.';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
""")

# Создание триггера
curs.execute("""
CREATE TRIGGER birth_death_check_trigger
BEFORE INSERT OR UPDATE ON people
FOR EACH ROW
EXECUTE FUNCTION check_birth_death_dates();
""")

con.commit()
con.close()

print("birth_death_check_trigger создан.")
