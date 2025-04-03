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
    ('Alice', 'Marie', 'Brown', '1990-07-21', 'Berlin', None, None, 'женский', 'Bio for Alice'),
    ('Robert', 'James', 'Wilson', '1972-03-03', 'Tokyo', None, None, 'мужской', 'Bio for Robert'),
    ('Emily', None, 'Davis', '2000-06-15', 'Moscow', None, None, 'женский', 'Bio for Emily'),
    ('Charles', 'Edward', 'Martinez', '1965-09-23', 'Madrid', None, None, 'мужской', 'Bio for Charles'),
    ('Sophia', None, 'Lopez', '1995-11-30', 'Rome', None, None, 'женский', 'Bio for Sophia'),
    ('Daniel', 'Henry', 'Garcia', '1988-04-17', 'Sydney', None, None, 'мужской', 'Bio for Daniel'),
    ('Olivia', None, 'Harris', '2012-12-01', 'Toronto', None, None, 'женский', 'Bio for Olivia')
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
    (4, 5, 'супруг', '2015-09-12', None),
    (6, 7, 'родитель-ребенок', None, None),
    (8, 9, 'супруг', '2018-04-22', None),
    (3, 10, 'родитель-ребенок', None, None),
    (7, 10, 'родитель-ребенок', None, None),
    (5, 6, 'брат-сестра', None, None),
    (2, 4, 'супруг', None, None)
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
    ('Diabetes', 'Genetic predisposition to diabetes'),
    ('Hypertension', 'High blood pressure risk'),
    ('Asthma', 'Respiratory condition often inherited'),
    ('Baldness', 'Pattern hair loss in men and women'),
    ('Left-handedness', 'Tendency to use the left hand more often'),
    ('Color Blindness', 'Difficulty distinguishing certain colors'),
    ("Alzheimer's Disease", 'Neurodegenerative disorder with genetic links')
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
    (4, 4, 'Yes', 'Runs in family'),
    (5, 5, 'No', 'No history in family'),
    (6, 6, 'Yes', 'Family predisposition'),
    (7, 7, 'Yes', 'Maternal grandfather was bald'),
    (8, 8, 'Yes', 'Several left-handed relatives'),
    (9, 9, 'Yes', 'Inherited from father'),
    (10, 10, 'No', 'No known cases in family')
]

for inheritance in inheritance_data:
    curs.execute(
        'INSERT INTO inheritance (person_id, trait_id, value, notes) VALUES (%s, %s, %s, %s);',
        inheritance
    )
con.commit()

con.close()
print('Data inserted')
