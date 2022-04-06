import pytest
from connection import execute_query
from demo import *
# from pgAdmin import abilities, ability_types, heroes, relationship_types, relationships
# from pgAdmin import public_tables 


def test_trial():
    x = 'check'
    assert x == 'check'

# def test_ability_types_exist():
#     ability = """
#     select name from ability_types
#     where name='Flying'
#     """
#     assert execute_query(ability)

# def test_table():
#     execute_query(create_table)
#     assert test is not None

def test_table():
    assert execute_query(create_table) == True

def test_get_a_hero():
    assert execute_query(select_heroes).fetchall() == True
    