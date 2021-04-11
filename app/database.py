from app import db
from sqlalchemy.sql import text

# calls SELECT query to display results from gyms table based on given gymname and univerity. Utilizes SQL alchemy.
# Returns a list from each tuple returned from query
def fetch_gyms(gymname: str, university: str) -> dict:
    conn = db.connect()
    if len(gymname) > 0 and len(university) > 0:
        statement = 'SELECT GymID, GymName, University, Capacity, Status FROM Gyms WHERE GymName LIKE "%{0}%" AND University LIKE "%{1}%" ORDER BY Status DESC, University ASC, GymName ASC;'.format(gymname, university)
    elif len(gymname) > 0:
        statement = 'SELECT GymID, GymName, University, Capacity, Status FROM Gyms WHERE GymName LIKE "%{0}%" ORDER BY Status DESC, University ASC, GymName ASC;'.format(gymname)
    elif len(university) > 0:
        statement = 'SELECT GymID, GymName, University, Capacity, Status FROM Gyms WHERE University LIKE "%{0}%" ORDER BY Status DESC, University ASC, GymName ASC;'.format(university)
    else:
        statement = 'SELECT GymID, GymName, University, Capacity, Status FROM Gyms ORDER BY Status DESC, University ASC, GymName ASC;'
    query = text(statement)
    print(query)
    query_results = conn.execute(query).fetchall()
    conn.close()
    gyms_list = []
    for result in query_results:
        item = {
            "GymID": result[0],
            "GymName": result[1],
            "University": result[2],
            "Capacity": result[3],
            "Status": result[4]
        }
        gyms_list.append(item)
    return gyms_list

def fetch_buddies(username: str) -> dict:
    conn = db.connect()
    if len(username) > 0:
        statement = 'SELECT u.FirstName, u.LastName, u.Email, g.GymName, g.University, r.StartTime, r.EndTime, r.Day, r.Month, r.Year FROM Users AS u NATURAL JOIN Reservations AS r JOIN Gyms AS g USING (GymID), (SELECT * FROM Reservations as cu WHERE cu.Username = "{0}") AS indi WHERE indi.Username != u.Username AND r.StartTime = indi.StartTime AND r.EndTime = indi.EndTime AND r.GymID = indi.GymID AND r.Day = indi.Day AND r.Month = indi.Month AND r.Year = indi.Year ORDER BY r.Year, r.Month, r.Day, u.LastName, u.FirstName;'.format(username)
    query = text(statement)
    print(query)
    query_results = conn.execute(query).fetchall()
    conn.close()
    buddy_list = []
    for result in query_results:
        item = {
            "FirstName": result[0],
            "LastName": result[1],
            "Email": result[2],
            "GymName": result[3],
            "University": result[4],
            "StartTime": result[5],
            "EndTime": result[6],
            "Day": result[7],
            "Month": result[8],
            "Year": result[9]
        }
        buddy_list.append(item)
    return buddy_list
  
def update_gym_name(GymID: int, text: str) -> None:
    conn = db.connect()
    query = 'Update Gyms set GymName = "{1}" where GymID = {0};'.format(text, GymID)
    conn.execute(query)
    conn.close()

def update_gym_uni(GymID: int, text: str) -> None:
    conn = db.connect()
    query = 'Update Gyms set University = "{1}" where GymID = {0};'.format(text, GymID)
    conn.execute(query)
    conn.close()
def update_gym_capacity(GymID: int, text:int) -> None:
    conn = db.connect()
    query = 'Update Gyms set Capacity = {1} where GymID = {0};'.format(text, GymID)
    conn.execute(query)
    conn.close()

def update_gym_status(GymID: int, text:str) -> None:
    conn = db.connect()
    query = 'Update Gyms set Status = "{1}" where GymID = {0};'.format(text, GymID)
    conn.execute(query)
    conn.close()

####

###
def insert_new_gym(GymName: str, University: str, Capacity: int, Status: str):
    conn = db.connect()
    query = 'Insert Into Gyms (GymName, University, Capacity, Status) VALUES ("{}", "{}", "{}", "{}");'.format(GymName, University, Capacity, Status)
    conn.execute(query)
    conn.close()


def remove_gym_by_id(GymID: int) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'Delete From Gyms where GymID={};'.format(GymID)
    conn.execute(query)
    conn.close()


def fetch_progress(exercise: str) -> dict:
    conn = db.connect()
    if len(exercise) > 0:
        statement = 'SELECT ProgressID, Exercise, Set_Size, Exercise_Stat FROM Progress WHERE Exercise LIKE "%{0}%" ORDER BY Exercise ASC;'.format(exercise)
    else:
        statement = 'SELECT ProgressID, Exercise, Set_Size, Exercise_Stat FROM Progress ORDER BY Exercise ASC;'
    query = text(statement)
    print(query)
    query_results = conn.execute(query).fetchall()
    conn.close()
    progress_list = []
    for result in query_results:
        item = {
            "ProgressID": result[0],
            "Exercise": result[1],
            "Set_Size": result[2],
            "Exercise_Stat": result[3]
        }
        progress_list.append(item)
    return progress_list


def fetch_progmax(exercise: str) -> dict:
    conn = db.connect()
    if len(exercise) > 0:
        statement = 'SELECT Exercise, MAX(Set_Size) From Users Natural Join Progress WHERE Exercise LIKE "%{0}%" GROUP BY Exercise'.format(exercise)
    query = text(statement)
    print(query)
    query_results = conn.execute(query).fetchall()
    conn.close()
    progmax_list = []
    for result in query_results:
        item = {
            "Exercise": result[0],
            "Max_Set_Size": result[1]
        }
        progmax_list.append(item)
    return progmax_list

def update_prog_exer(exercise: str, ProgressID:int) -> None:
    conn = db.connect()
    query = 'Update Progress set Exercise = "{0}" where ProgressID = {1};'.format(exercise, ProgressID)
    conn.execute(query)
    conn.close()
def update_prog_set(set_size: int, ProgressID:int) -> None:
    conn = db.connect()
    query = 'Update Progress set Set_Size = {0} where ProgressID = {1};'.format(set_size, ProgressID)
    conn.execute(query)
    conn.close()

def update_prog_stat(exercise_stat: int, ProgressID:int) -> None:
    conn = db.connect()
    query = 'Update Progress set Exercise_Stat = {0} where ProgressID = {1};'.format(exercise_stat, ProgressID)
    conn.execute(query)
    conn.close()

def insert_new_progress(ProgressID: int, Exercise: str, Set_Size: int, Exercise_Stat: int):
    conn = db.connect()
    query = 'Insert Into Progress (ProgressID, Exercise, Set_Size, Exercise_Stat) VALUES ("{}", "{}", "{}", "{}");'.format(ProgressID, Exercise, Set_Size, Exercise_Stat)
    conn.execute(query)
    conn.close()

def remove_progress_by_id(ProgressID: int) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'Delete From Progress where ProgressID={};'.format(ProgressID)
    conn.execute(query)
    conn.close()