import psycopg2

con = psycopg2.connect(
    dbname='family_trees_db',
    user='postgres',
    password='1231',
    host='localhost',
    port='5432'
)

curs = con.cursor()

curs.execute("DROP TRIGGER IF EXISTS blood_type_validation_trigger ON inheritance;")
curs.execute("DROP FUNCTION IF EXISTS validate_blood_type();")

curs.execute("""
CREATE OR REPLACE FUNCTION validate_blood_type()
RETURNS TRIGGER AS $$
DECLARE
    valid_types TEXT[] := ARRAY['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'];
    trait_name TEXT;
BEGIN
    SELECT trait_name INTO trait_name FROM traits WHERE id = NEW.trait_id;

    IF trait_name = 'Blood Type' AND NOT (NEW.value = ANY (valid_types)) THEN
        RAISE EXCEPTION 'Недопустимое значение группы крови: %', NEW.value;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
""")

curs.execute("""
CREATE TRIGGER blood_type_validation_trigger
BEFORE INSERT OR UPDATE ON inheritance
FOR EACH ROW
EXECUTE FUNCTION validate_blood_type();
""")

con.commit()
con.close()

print("blood_type_validation_trigger создан.")
