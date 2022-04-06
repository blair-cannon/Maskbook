import sys
sys.path.append("/workspace/Maskbook")
from connection import select_one, select_all, run_this

# all of these are made in relation to the test tables to not disturb the real environment until production
# DELETE data:

# 1. A treatment came out that cured Mental Mary's narcolepsy so we can delete it as a weakness

delete_a_weakness_type = """ 
DELETE FROM weakness_types WHERE name = 'Narcolepsy'
"""

# run_this(delete_a_weakness_type)



# 2. There has been some drama between two Super Heroes. They don't want to identify as enemies 
# on Maskbook for everyone to see, so they unfriend each other.

delete_a_relationship = """ 
DELETE FROM test_relationships 
WHERE hero1_id = 2 AND hero2_id = 1
"""

run_this(delete_a_relationship)


