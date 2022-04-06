import sys
sys.path.append("/workspace/Maskbook")
from connection import select_one, select_all, run_this

# all of these are made in relation to the test tables to not disturb the real environment until production
# UPDATE data:

# 1. Update an existing table: 

add_strength_rankings = """ 
ALTER TABLE test_abilities
ADD strength_index int
"""
run_this(add_strength_rankings)

# 2. Update existing records in the table to now have strength rankings

update_with_strengths = """ 
UPDATE test_abilities
SET strength_index = 5
WHERE hero_id = 1;

UPDATE test_abilities
SET strength_index = 3
WHERE hero_id = 2 AND ability_type_id = 3;

UPDATE test_abilities
SET strength_index = 7
WHERE hero_id = 2 AND ability_type_id = 4;

UPDATE test_abilities
SET strength_index = 2
WHERE hero_id = 3;

UPDATE test_abilities
SET strength_index = 10
WHERE hero_id = 4 AND ability_type_id = 2;

UPDATE test_abilities
SET strength_index = 4
WHERE hero_id = 4 AND ability_type_id = 6;

UPDATE test_abilities
SET strength_index = 10
WHERE hero_id = 5;

UPDATE test_abilities
SET strength_index = 8
WHERE hero_id = 6;

UPDATE test_abilities
SET strength_index = 9
WHERE hero_id = 7;
"""
run_this(update_with_strengths)