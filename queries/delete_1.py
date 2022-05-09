import sys
sys.path.append("/workspace/Maskbook")
from connection import select_one, select_all, run_this

# DELETE data:

# 1. A treatment came out that cured Mental Mary's narcolepsy so we can delete it as a weakness

delete_a_weakness_type = """ 
DELETE FROM weakness_types WHERE name = 'Narcolepsy'
"""

# run_this(delete_a_weakness_type)



# 2. There has been some drama between two Super Heroes. They don't want to identify as enemies 
# on Maskbook for everyone to see, so they unfriend each other.

delete_a_relationship = """ 
DELETE FROM relationships 
WHERE hero1_id = 2 AND hero2_id = 1
"""

# run_this(delete_a_relationship)


# 3. Delete a profile. He is going undercover and needs to delete all of his social media accounts. 

delete_a_profile = """ 
DELETE FROM heroes
WHERE name = 'blair'
"""

run_this(delete_a_profile)