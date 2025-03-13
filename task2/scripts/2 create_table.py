import psycopg2

con = psycopg2.connect(
    dbname='family_trees_db',
    user='postgres',
    password='1231',
    host='localhost',
    port='5432'
)

curs = con.cursor()

create_tables_queries = [
    '''
    CREATE TABLE IF NOT EXISTS people (
        person_id SERIAL PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL,
        middle_name VARCHAR(255),
        last_name VARCHAR(255) NOT NULL,
        birth_date DATE,
        birth_place VARCHAR(255),
        death_date DATE,
        death_place VARCHAR(255),
        gender VARCHAR(20) CHECK (gender IN ('мужской', 'женский', 'другое', 'неизвестно')),
        bio TEXT,
        photo VARCHAR(255)
    );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS relationships (
        relationship_id SERIAL PRIMARY KEY,
        person1_id INTEGER REFERENCES people(person_id) NOT NULL,
        person2_id INTEGER REFERENCES people(person_id) NOT NULL,
        relationship_type VARCHAR(50) CHECK (relationship_type IN ('родитель-ребенок', 'супруг', 'брат-сестра', 'другое')),
        start_date DATE,
        end_date DATE
    );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS traits (
        trait_id SERIAL PRIMARY KEY,
        trait_name VARCHAR(255) NOT NULL,
        description TEXT
    );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS inheritance (
        inheritance_id SERIAL PRIMARY KEY,
        person_id INTEGER REFERENCES people(person_id) NOT NULL,
        trait_id INTEGER REFERENCES traits(trait_id) NOT NULL,
        value VARCHAR(255),
        notes TEXT
    );
    '''
]

for query in create_tables_queries:
    curs.execute(query)
con.commit()

con.close()
print('Tables created')