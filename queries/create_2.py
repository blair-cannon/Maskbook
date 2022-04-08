import sys
sys.path.append("/workspace/Maskbook")
from connection import select_one, select_all, run_this

# creat new data:
 
# 3. create new hero
new_hero = """ 
INSERT INTO heroes (name, about_me, biography)
VALUES ('Antonio', 'The best character of any great movie', 'Got a topic? Any topic? This mans has a cool story about it. And he bakes. And he plays Magic. Nuf said.')
"""
run_this(new_hero)

# 4. create new ability_type
new_ability_type = """ 
INSERT INTO ability_types (name)
VALUES ('Vampire')
"""
run_this(new_ability_type)

# 5. create new ability
new_ability = """ 
INSERT INTO abilities (hero_id, ability_type_id)
VALUES (
 (SELECT id FROM heroes WHERE name = 'Antonio'),
 (SELECT id FROM ability_types WHERE name = 'Vampire' )
 )
"""
run_this(new_ability)

# 6. create new relationship_type
new_relationship_type = """ 
INSERT INTO relationship_types (name)
VALUES ('Super Team')
"""
run_this(new_relationship_type)

# 7. create new relationship
new_relationship = """ 
INSERT INTO relationships (hero1_id, hero2_id, relationship_type_id)
VALUES (
    (SELECT id FROM heroes WHERE name = 'The Hummingbird'),
    (SELECT id FROM heroes WHERE name = 'Antonio'),
    (SELECT id FROM relationship_types WHERE name = 'Super Team')
    )
"""
run_this(new_relationship)