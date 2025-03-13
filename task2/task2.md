# Лабораторная работа №2

* Имя студента: Андрей Соснов
* Группа: P4150
* Дата выполнения задания: 13.03.2025
* Наименование дисциплины: Взаимодействие с базами данных
* Текст задания:
* Описание предметной области:

Предметная область включает в себя генеалогическое дерево, реализованное в веб и мобильном приложениях, которое позволяет пользователю отразить в нём всевозможные родственные связи с другими людьми, а также проследить наследование какого-либо признака (в том числе заболевания, но не только) и рассчитать вероятность проявления этого признака в последующих поколениях.

Приложение подразумевает наличие нескольких моделей (сущностей, классов), которые будут отражать данную предметную область и конкретно будут реализованы в таблицах реляционной базы данных.
Список сущностей
Классификация сущностей:
1.
Люди (People):
* Тип: Стержневая сущность.
* Описание: Основная сущность, представляющая индивидуумов в генеалогическом дереве. Содержит ключевую информацию о каждом человеке.
2.
Связи (Relationships):
* Тип: Ассоциативная сущность.
* Описание: Отражает отношения между людьми. Связывает две стержневые сущности (Люди) и описывает тип их связи.
3.
Признаки (Traits):
* Тип: Стержневая сущность.
* Описание: Представляет собой набор характеристик, которые могут наследоваться.
4.
Наследование (Inheritance):
* Тип: Ассоциативная сущность.
* Описание: Описывает, как признаки наследуются от одного человека к другому. Связывает стержневые сущности (Люди и Признаки). Содержит информацию о значении признака у конкретного человека и дополнительные заметки.

ER-диаграмма

```mermaid
erDiagram
    PEOPLE {
        int person_id PK
        varchar first_name
        varchar middle_name
        varchar last_name
        date birth_date
        varchar birth_place
        date death_date
        varchar death_place
        varchar gender
        text bio
        varchar photo
        int user_id FK
    }
    RELATIONSHIPS {
        int relationship_id PK
        int person1_id FK
        int person2_id FK
        varchar relationship_type
        date start_date
        date end_date
    }
    TRAITS {
        int trait_id PK
        varchar trait_name
        text description
    }
    INHERITANCE {
        int inheritance_id PK
        int person_id FK
        int trait_id FK
        varchar value
        text notes
    }
Даталогическая модель:
1. Таблица: Люди (people)
• person_id (SERIAL PRIMARY KEY)
• first_name (VARCHAR(255) NOT NULL)
• middle_name (VARCHAR(255))
• last_name (VARCHAR(255) NOT NULL)
• birth_date (DATE)
• birth_place (VARCHAR(255))
• death_date (DATE)
• death_place (VARCHAR(255))
• gender (VARCHAR(20) CHECK (gender IN ('мужской', 'женский', 'неизвестно')))
• bio (TEXT)
• photo (VARCHAR(255))
2. Таблица: Связи (relationships)
• relationship_id (SERIAL PRIMARY KEY)
• person1_id (INTEGER REFERENCES people(person_id) NOT NULL)
• person2_id (INTEGER REFERENCES people(person_id) NOT NULL)
• relationship_type (VARCHAR(50))
• start_date (DATE)
• end_date (DATE)
3. Таблица: Признаки (traits)
• trait_id (SERIAL PRIMARY KEY)
• trait_name (VARCHAR(255) NOT NULL)
• description (TEXT)
4. Таблица: Наследование (inheritance)
• inheritance_id (SERIAL PRIMARY KEY)
• person_id (INTEGER REFERENCES people(person_id) NOT NULL)
• trait_id (INTEGER REFERENCES traits(trait_id) NOT NULL)
• value (VARCHAR(255))
• notes (TEXT)
