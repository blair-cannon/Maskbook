import sys
sys.path.append("/workspace/Maskbook")
from connection import select_one, select_all, run_this

# READ data:

# GOAL: Select any heroes (if any) that have more disabilities than abilities (can view with angry cat)

# 1. select any heroes that have more than one ability
find_heros_with_more_than_one_ability = """ 
SELECT hero_id, COUNT(hero_id)
FROM abilities
GROUP BY hero_id
HAVING COUNT(hero_id)>1
"""
double_abilities = select_all(find_heros_with_more_than_one_ability)
# first number = hero_id
# second number = count:
print(double_abilities)

# 2. select any heroes that have more than one weakness
find_heros_with_more_than_one_weakness = """ 
SELECT hero_id, COUNT(hero_id)
FROM weaknesses
GROUP BY hero_id
HAVING COUNT(hero_id)>1
"""
double_weaknesses = select_all(find_heros_with_more_than_one_weakness)
print(double_weaknesses) 

# 3. compare hero_id's of the hero's with > 1 ability 
# to the hero's with > 1 weakness
# if any heroes show up in both lists, compare the counts
# to see if the hero has more abilities or disabilities
# otherwise, if a hero only appears in the double_weaknesses list
# then it automatically has more weaknesses than abilities 
# and no comparison is needed
result = 0
for strong_hero in double_abilities:
    for weak_hero in double_weaknesses:
        if weak_hero[0] == strong_hero[0]:
                if weak_hero[1] > strong_hero[1]:
                    result = weak_hero[0]
                else: 
                    print('There are no heroes with more weaknesses than abilities.')
        else:
            result = weak_hero[0]
            # print(result)


# 4. Convert hero_id to hero_name 

print(result)
find_name = """ 
    SELECT name FROM heroes 
    WHERE id={}
    """.format(result)
name = select_one(find_name)
print(''.join(name)) # This hero has more weaknesses than abilities. 

