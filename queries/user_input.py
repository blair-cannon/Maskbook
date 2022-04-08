import sys
sys.path.append("/workspace/Maskbook")
from connection import select_one, select_all, run_this

# interactive terminal code

def find_info(INPUT_NAME, INFO_NEEDED):
    try:
        sql = """ 
        SELECT {} FROM heroes
        WHERE name = '{}'
        """.format(INFO_NEEDED, INPUT_NAME)
        info = select_one(sql)
        print(''.join(info))
    except: 
        print("Let's try that again, we couldn't find that hero.")
        init()

def find_abilities(INPUT_NAME):
    try:
        sql = """ 
        SELECT heroes.name as Name, STRING_AGG(ability_types.name, ', ') AS Ability
        FROM heroes
        JOIN abilities
        ON heroes.id = abilities.hero_id
        JOIN ability_types
        ON abilities.ability_type_id = ability_types.id
        WHERE heroes.name = '{}'
        GROUP BY heroes.name       
        """.format(INPUT_NAME)
        abilities_tuple = select_one(sql)
        print(''.join(abilities_tuple[1]))
    except:
        print("There seems to be a problem. Let's try that again.")
        init()

def find_weaknesses(INPUT_NAME):
    try:
        sql = """ 
        SELECT heroes.name as Name, STRING_AGG(weakness_types.name, ', ') AS Weaknesses
        FROM heroes
        JOIN weaknesses
        ON heroes.id = weaknesses.hero_id
        JOIN weakness_types
        ON weaknesses.weakness_type_id = weakness_types.id
        WHERE heroes.name = '{}'
        GROUP BY heroes.name       
        """.format(INPUT_NAME)
        weakness_tuple = select_one(sql)
        print(''.join(weakness_tuple[1]))
    except:
        print("There seems to be a problem. Let's try that again.")
        init()

def find_relationships(INPUT_NAME, INFO_NEEDED):
    try: 
        sql = """
        SELECT h1.name AS hero1, h2.name AS hero2, relationship_types.name AS Relationship
        FROM relationships 
        JOIN heroes h1
        ON h1.id = relationships.hero1_id 
        JOIN heroes h2 
        ON h2.id = relationships.hero2_id
        JOIN relationship_types
        ON relationships.relationship_type_id = relationship_types.id
        WHERE (h1.name = '{}' OR h2.name = '{}') AND relationship_types.name = '{}'
        """.format(INPUT_NAME, INPUT_NAME, INFO_NEEDED)
        friends_tuple = select_all(sql)
        # print(friends_tuple)
        friends = []
        for friendship in friends_tuple:
            if friendship[0] == INPUT_NAME:
                if friendship[1] not in friends:
                    friends.append(friendship[1])
            elif friendship[1] == INPUT_NAME:
                if friendship[0] not in friends:
                    friends.append(friendship[0])
        print(', '.join(friends))
    except:
        print("There seems to be a problem. Let's try that again.")
        init()

def show_all():
    try: 
        sql = """ 
        SELECT name FROM heroes
        """
        heroes_tuple = select_all(sql)
        print(heroes_tuple)
        # can't get this to turn into a string for the life of me
    except:
        print("There seems to be a problem. Let's try that again.")
        init()
    
def new_hero(new_name, new_about, new_bio):
    try:
        sql = """ 
        INSERT INTO heroes(name, about_me, biography)
        VALUES ('{}','{}','{}')
        """.format(new_name, new_about, new_bio)
        run_this(sql)
    except:
            print("There seems to be a problem. Let's try that again.")
            init()

def add_relationship(user_name, new_relationship_id, user_friend):
    try:
        sql1 = """ 
        SELECT id FROM heroes 
        WHERE name = '{}'
        """.format(user_name)
        user_id_tuple = select_one(sql1)
        user_id = user_id_tuple[0]

        sql2 = """ 
        SELECT id FROM heroes 
        WHERE name = '{}'
        """.format(user_friend)
        other_id_tuple = select_one(sql2)
        other_id = other_id_tuple[0]
        
        sql = """ 
        INSERT INTO relationships(hero1_id, hero2_id, relationship_type_id)
        VALUES ('{}','{}','{}')
        """.format(user_id, other_id, new_relationship_id)
        run_this(sql)
    except:
        print("There seems to be a problem. Let's try that again.")
        init()

def init():   

    print("Welcome to MaskBook. \n A place where all supernaturals are welcomed and encouraged to unMask and let loose.")

    GOAL = input("What can we help you with? \n Choose from the following: \n FIND HERO \n MAKE NEW PROFILE \n ADD NEW RELATIONSHIP \n ")

    if GOAL.lower() == "find hero": 
        FILTER_BY = input("Would you like to search by name?")
        if FILTER_BY.lower() == 'yes':
            INPUT_NAME = input("Enter the name of the hero you are looking for:")
            INFO_NEEDED = input("What info would you like to search? \n Choose from the following: \n About Me Statement \n Biography \n Abilities \n Weaknesses \n Friends \n Enemies \n")
        
            if INFO_NEEDED.lower() == 'about me statement':
                INFO_NEEDED = 'about_me'
                find_info(INPUT_NAME, INFO_NEEDED)

            elif INFO_NEEDED.lower() == 'biography':
                find_info(INPUT_NAME, INFO_NEEDED)

            elif INFO_NEEDED.lower() == 'abilities':
                find_abilities(INPUT_NAME)

            elif INFO_NEEDED.lower() == 'weaknesses':
                find_weaknesses(INPUT_NAME)

            elif INFO_NEEDED.lower() == 'friends':
                INFO_NEEDED = 'Friend'
                find_relationships(INPUT_NAME, INFO_NEEDED)
        
            elif INFO_NEEDED.lower() == 'enemies':
                INFO_NEEDED = 'Enemy'
                find_relationships(INPUT_NAME, INFO_NEEDED)
            else: 
                print("I'm sorry, we don't do that here. Try again.")
                init()
        elif FILTER_BY.lower() == 'no':
            SEE_LIST = input("Would you like to see a list of the heroes?")
            if SEE_LIST.lower() == 'yes':
                show_all()
        else: 
            print("Sorry, we don't have that option. Try again.")
            init()
    elif GOAL.lower() == "make new profile":
        print("Perfect. Let's make a new profile!")
        new_name = input("What is your name?")
        new_about = input("What is your catch line? A simple sentence will do.")
        new_bio = input("Tell us a little more about yourself using 2-3 sentences.")
        new_hero(new_name, new_about, new_bio)


    elif GOAL.lower() == 'add new relationship':
        print("Perfect! Let's update your relationships.")
        user_name = input("What is your name?")
        user_relationship = input("Would you like to add a friend or enemy?")
        if user_relationship.lower() == 'friend':
            new_relationship_id = 1
        elif user_relationship.lower() == 'enemy':
            new_relationship_id = 2
        user_friend = input("What is their name?")
        add_relationship(user_name, new_relationship_id, user_friend)
        
init()