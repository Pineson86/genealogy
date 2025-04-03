# Лабораторная работа №2

* **Имя студента:** Андрей Соснов  
* **Группа:** P4150  
* **Дата выполнения задания:** 13.03.2025  
* **Наименование дисциплины:** Взаимодействие с базами данных  

## Текст задания

### Описание предметной области

Предметная область включает в себя генеалогическое дерево, реализованное в веб и мобильном приложениях, которое позволяет пользователю отразить в нём всевозможные родственные связи с другими людьми, а также проследить наследование какого-либо признака (в том числе заболевания, но не только) и рассчитать вероятность проявления этого признака в последующих поколениях.

Приложение подразумевает наличие нескольких моделей (сущностей), которые будут отражать данную предметную область и конкретно будут реализованы в таблицах реляционной базы данных.

### Список сущностей

#### Классификация сущностей

1. **Люди (People)**  
   * *Тип:* Стержневая сущность.  
   * *Описание:* Основная сущность, представляющая индивидуумов в генеалогическом дереве. Содержит ключевую информацию о каждом человеке.

2. **Связи (Relationships)**  
   * *Тип:* Ассоциативная сущность.  
   * *Описание:* Отражает отношения между людьми. Связывает две стержневые сущности (Люди) и описывает тип их связи.

3. **Признаки (Traits)**  
   * *Тип:* Стержневая сущность.  
   * *Описание:* Представляет собой набор характеристик, которые могут наследоваться.

4. **Наследование (Inheritance)**  
   * *Тип:* Ассоциативная сущность.  
   * *Описание:* Описывает, как признаки наследуются от одного человека к другому. Связывает стержневые сущности (Люди и Признаки). Содержит информацию о значении признака у конкретного человека и дополнительные заметки.

## ER-диаграмма

```mermaid
erDiagram
    PEOPLE {
        SERIAL person_id PK
        VARCHAR(255) first_name NOT NULL
        VARCHAR(255) middle_name
        VARCHAR(255) last_name NOT NULL
        DATE birth_date
        VARCHAR(255) birth_place
        DATE death_date
        VARCHAR(255) death_place
        VARCHAR(20) gender CHECK (gender IN ('мужской', 'женский', 'неизвестно'))
        TEXT bio
        VARCHAR(255) photo
    }
    
    RELATIONSHIPS {
        SERIAL relationship_id PK
        INTEGER person1_id FK REFERENCES PEOPLE(person_id) NOT NULL
        INTEGER person2_id FK REFERENCES PEOPLE(person_id) NOT NULL
        VARCHAR(50) relationship_type
        DATE start_date
        DATE end_date
    }
    
    TRAITS {
        SERIAL trait_id PK
        VARCHAR(255) trait_name NOT NULL
        TEXT description
    }
    
    INHERITANCE {
        SERIAL inheritance_id PK
        INTEGER person_id FK REFERENCES PEOPLE(person_id) NOT NULL
        INTEGER trait_id FK REFERENCES TRAITS(trait_id) NOT NULL
        VARCHAR(255) value
        TEXT notes
    }
    
    PEOPLE ||--o{ RELATIONSHIPS : "has relationships"
    PEOPLE ||--o{ INHERITANCE : "inherits traits"
    TRAITS ||--o{ INHERITANCE : "is inherited by"
