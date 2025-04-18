# Лабораторная работа №3

* Имя студента: Андрей Соснов
* Группа: P4150
* Дата выполнения задания: 03.04.2025
* Наименование дисциплины: Взаимодействие с базами данных
* Текст задания:
* Описание предметной области:

Предметная область включает в себя генеалогическое дерево, реализованное в веб и мобильном приложениях, которое позволяет пользователю отразить в нём всевозможные родственные связи с другими людьми, а также проследить наследование какого-либо признака (в том числе заболевания, но не только) и рассчитать вероятность проявления этого признака в последующих поколениях.

Приложение подразумевает наличие нескольких моделей (сущностей, классов), которые будут отражать данную предметную область и конкретно будут реализованы в таблицах реляционной базы данных.

# Актуальная даталогическая модель
```mermaid
classDiagram
    class people {
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
        text photo
    }

    class relationships {
        int relationship_id PK
        int person1_id FK
        int person2_id FK
        varchar relationship_type
        date start_date
        date end_date
    }

    class traits {
        int trait_id PK
        varchar trait_name
        text description
    }

    class inheritance {
        int inheritance_id PK
        int person_id FK
        int trait_id FK
        varchar value
        text notes
    }

    people "1" -- "0..*" relationships : person1_id
    people "1" -- "0..*" relationships : person2_id
    people "1" -- "0..*" inheritance : person_id
    traits "1" -- "0..*" inheritance : trait_id

# Анализ функциональных зависимостей

1.  **Таблица "Люди" (people):**

    * **Зависимость:** `person_id` → `first_name`, `middle_name`, `last_name`, `birth_date`, `birth_place`, `death_date`, `death_place`, `gender`, `bio`, `photo`.
    * **Объяснение:** Значение `person_id` однозначно определяет все остальные атрибуты человека. Каждый `person_id` соответствует только одному набору значений остальных атрибутов.
    * **Значение:** Эта зависимость является ключевой, так как `person_id` является первичным ключом таблицы. Она гарантирует уникальность каждой записи и целостность данных.

2.  **Таблица "Признаки" (traits):**

    * **Зависимость:** `trait_name` → `description`.
    * **Объяснение:** Название признака однозначно определяет его описание. Каждый `trait_name` соответствует только одному `description`.
    * **Значение:** Эта зависимость показывает, что описание признака является неотъемлемой частью информации о признаке.

3.  **Таблица "Наследование" (inheritance):**

    * **Зависимость:** `person_id`, `trait_id` → `value`, `notes`.
    * **Объяснение:** Комбинация `person_id` и `trait_id` однозначно определяет значение признака (`value`) и заметки (`notes`) для конкретного человека.
    * **Значение:** Эта зависимость показывает, как признаки наследуются от одного человека к другому. Комбинация `person_id` и `trait_id` является составным ключом, который обеспечивает уникальность каждой записи о наследовании.

