# SELECT abilities.hero_id, abilities.ability_type_id, ability_types.name
# FROM abilities
# INNER JOIN ability_types ON abilities.ability_type_id=ability_types.id

# SELECT  heroes.name AS heroes, STRING_AGG(ability_types.name, ', ') AS Ability
# FROM heroes
# JOIN abilities
# ON heroes.id = abilities.hero_id
# JOIN ability_types
# ON abilities.ability_type_id = ability_types.id
# GROUP BY heroes.name


# SELECT h1.name AS hero1, h2.name AS hero2, relationship_types.name AS Relationship
# FROM relationships 
# JOIN heroes h1
# ON h1.id = relationships.hero1_id 
# JOIN heroes h2 
# ON h2.id = relationships.hero2_id
# JOIN relationship_types
# ON relationships.relationship_type_id = relationship_types.id