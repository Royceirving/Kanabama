from werkzeug.security import generate_password_hash, check_password_hash

def make_new_team_query_generator(team_name):
    return """
    CREATE TABLE {}(
        id integer primary key NOT NULL,
        name varchar(64) NOT NULL,
        description varchar(512),
        priority integer NOT NULL,
        date TEXT,
        state integer NOT NULL
    )""".format(team_name)

def make_team_table_query_generator():
    return """
    CREATE TABLE teams(
        id integer primary key NOT NULL,
        name varchar(64) unique NOT NULL,
        password_hash varchar(128) NOT NULL
    )
    """

def place_new_team_into_teams(team_name,password):
    return """
    INSERT INTO teams(name,password_hash)
    VALUES('{}','{}')
    """.format(team_name,generate_password_hash(password))

def place_new_user_gererator(username,password,teamname):
    return """
    INSERT INTO user(username,password_hash,teamname)
    VALUES('{}','{}','{}')
    """.format(username,generate_password_hash(password),teamname)

def get_stories_for_team(teamname):
    return """
    SELECT * FROM {}
    """.format(teamname)

def commit_story_generator(team_name,story_name,description="",priority=0,date='',state=0):
    return """
    INSERT INTO {}(name,description,priority,date,state)
    VALUES('{}','{}','{}','{}','{}')
    """.format(team_name,story_name,description,priority,date,state)

def delete_story_in_team_generator(team_name,story_id):
    return "DELETE FROM {} WHERE id == {}".format(team_name,story_id)