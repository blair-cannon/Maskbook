import sys
sys.path.append("/workspace/Maskbook")
from connection import select_one, select_all, run_this

# all of these are made in relation to the test tables to not disturb the real environment until production
# create new tables:


# Heroes are encouraged to be vulnerable on MaskBook and share about their weaknesses. 
# 1. A table that defines different weaknesses:
create_weakness_types = """
   CREATE TABLE weakness_types (
        id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        name VARCHAR(64)
    );
INSERT INTO
    weakness_types (name)
VALUES
    ('Kryptonite');

INSERT INTO
    weakness_types (name)
VALUES
    ('High Pitch Frequency');

INSERT INTO
    weakness_types (name)
VALUES
    ('Lack of water');

INSERT INTO
    weakness_types (name)
VALUES
    ('Intense Cold');

INSERT INTO
    weakness_types (name)
VALUES
    ('Narcolepsy');

INSERT INTO
    weakness_types (name)
VALUES
    ('Seasonal Allergies');

INSERT INTO
    weakness_types (name)
VALUES
    ('Social Anxiety');
    """
run_this(create_weakness_types)

# 2. A table that displays which heroes have which weaknesses:
create_weaknesses = """
CREATE TABLE weaknesses (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    hero_id INTEGER NOT NULL,
    FOREIGN KEY (hero_id) REFERENCES test_heroes (id) ON DELETE CASCADE,
    weakness_type_id INTEGER NOT NULL,
    FOREIGN KEY (weakness_type_id) REFERENCES test_ability_types (id) ON DELETE CASCADE
);

INSERT INTO
    weaknesses (hero_id, weakness_type_id)
VALUES
    (1, 1);

INSERT INTO
    weaknesses (hero_id, weakness_type_id)
VALUES
    (2, 2);

INSERT INTO
    weaknesses (hero_id, weakness_type_id)
VALUES
    (3, 3);

INSERT INTO
    weaknesses (hero_id, weakness_type_id)
VALUES
    (3, 1);

INSERT INTO
    weaknesses (hero_id, weakness_type_id)
VALUES
    (4, 4);

INSERT INTO
    weaknesses (hero_id, weakness_type_id)
VALUES
    (5, 5);

INSERT INTO
    weaknesses (hero_id, weakness_type_id)
VALUES
    (6, 6);

    """

run_this(create_weaknesses)