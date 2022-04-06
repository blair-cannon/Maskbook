from connection import execute_query

# create new tables:

# A table that defines different weaknesses:
crete_weakness_types = """
   CREATE TABLE weakness_types (
        id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        name VARCHAR(64)
    );
INSERT INTO
    weakness_types (name)
VALUES
    ('Super Strength');

INSERT INTO
    weakness_types (name)
VALUES
    ('Flying');

INSERT INTO
    weakness_types (name)
VALUES
    ('Telekinesis');

INSERT INTO
    weakness_types (name)
VALUES
    ('Telepathy');

INSERT INTO
    weakness_types (name)
VALUES
    ('Frost Breath');

INSERT INTO
    weakness_types (name)
VALUES
    ('Super Speed');

INSERT INTO
    weakness_types (name)
VALUES
    ('Super Vision');
    """
execute_query(create_weakness_types)

# A table that displays which heroes have which weaknesses:
