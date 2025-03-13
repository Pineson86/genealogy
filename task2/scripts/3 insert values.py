import psycopg2

con = psycopg2.connect(
    dbname='family_trees_db',
    user='postgres',
    password='1231',
    host='localhost',
    port='5432'
)

curs = con.cursor()

# Заполнение таблицы people
people_data = [
    ('John', 'Michael', 'Doe', '1980-01-01', 'New York', None, None, 'мужской', 'Some bio'),
    ('Jane', None, 'Smith', '1985-05-15', 'London', '2020-10-20', 'London', 'женский', 'Another bio'),
    ('David', 'Lee', 'Johnson', '1955-12-10', 'Paris', '2015-08-05', 'Paris', 'мужской', 'Old bio'),
]

for person in people_data:
    curs.execute(
        'INSERT INTO people (first_name, middle_name, last_name, birth_date, birth_place, death_date, death_place, gender, bio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);',
        person
    )
con.commit()

# Заполнение таблицы relationships
relationships_data = [
    (1, 2, 'супруг', '2010-06-01', '2020-10-20'),
    (1, 3, 'родитель-ребенок', None, None),
    (2, 3, 'родитель-ребенок', None, None),
]

for relationship in relationships_data:
    curs.execute(
        'INSERT INTO relationships (person1_id, person2_id, relationship_type, start_date, end_date) VALUES (%s, %s, %s, %s, %s);',
        relationship
    )
con.commit()

# Заполнение таблицы traits
traits_data = [
    ('Eye Color', 'Color of the eyes'),
    ('Blood Type', 'A, B, AB or O'),
    ('Height', 'Height of the person'),
]

for trait in traits_data:
    curs.execute(
        'INSERT INTO traits (trait_name, description) VALUES (%s, %s);',
        trait
    )
con.commit()

# Заполнение таблицы inheritance
inheritance_data = [
    (1, 1, 'Blue', 'Inherited from father'),
    (2, 2, 'A+', 'Inherited from mother'),
    (3, 3, '180 cm', 'Tall family'),
]

for inheritance in inheritance_data:
    curs.execute(
        'INSERT INTO inheritance (person_id, trait_id, value, notes) VALUES (%s, %s, %s, %s);',
        inheritance
    )
con.commit()

con.close()
print('Data inserted')