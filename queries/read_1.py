import sys
sys.path.append("/workspace/Maskbook")
from connection import select_one, select_all, run_this

# all of these are made in relation to the test tables to not disturb the real environment until production
# read data:

# select any heroes (if any) that have more disabilities than abilities (can view with angry cat)

# select any heroes that have more than one ability
find_heros_with_more_than_one_ability = """ 
SELECT hero_id, COUNT(hero_id)
FROM test_abilities
GROUP BY hero_id
HAVING COUNT(hero_id)>1
"""
double_abilities = select_all(find_heros_with_more_than_one_ability)
# first number = hero_id
# second number = count:
print(double_abilities)

# select any heroes that have more than one weakness
find_heros_with_more_than_one_weakness = """ 
SELECT hero_id, COUNT(hero_id)
FROM weaknesses
GROUP BY hero_id
HAVING COUNT(hero_id)>1
"""
double_weaknesses = select_all(find_heros_with_more_than_one_weakness)
print(double_weaknesses) 

# compare hero_id's of the hero's with > 1 ability 
# to the hero's with > 1 weakness
# if any heroes show up in both lists, compare the counts
# to see if the hero has more abilities or disabilities
# otherwise, if a hero only appears in the double_weaknesses list
# then it automatically has more weaknesses than abilities 
# and no comparison is needed
for strong_hero in double_abilities:
    for weak_hero in double_weaknesses:
        if weak_hero[0] == strong_hero[0]:
                if weak_hero[1] > strong_hero[1]:
                    print(weak_hero[0])
                else: 
                    print('There are no heroes with more weaknesses than abilities.')
        else:
            print(weak_hero[0])


