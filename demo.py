# This is why you'll execute a series of SQL statements during demo day.
from connection import execute_query

# select_heroes = """
#     SELECT * FROM heroes
#     ORDER BY id DESC 
# """

# heroes = execute_query(select_heroes).fetchall()
# for hero in heroes:
#     print(hero[1])

# create_table = """
#     create table test (
#         test1 varchar,
#         test2 varchar
#     )
#     """

# execute_query(create_table)


# drop_table = """
#     drop table test
#     """

# execute_query(drop_table)

select_heroes = """
    SELECT * FROM heroes
    ORDER BY id DESC 
"""

heroes = execute_query(select_heroes)
for hero in heroes:
    print(hero[1])