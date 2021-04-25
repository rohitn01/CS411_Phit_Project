from app import db
from sqlalchemy.sql import text


def check_login(username: str, password: str) -> int:
    conn = db.connect()
    statement = 'SELECT COUNT(*) FROM Users WHERE Username = "{0}" AND Password = "{1}";'.format(username, password)
    query = text(statement)
    print(query)
    query_results = conn.execute(query).fetchall()
    conn.close()
    result = query_results[0][0]
    return result

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


def insert_new_gym(GymName: str, University: str, Capacity: int, Status: str):
    conn = db.connect()
    query = 'Insert Into Gyms (GymName, University, Capacity, Status) VALUES ("{}", "{}", "{}", "{}");'.format(GymName, University, Capacity, Status)
    conn.execute(query)
    conn.close()

def remove_gym_by_id(GymID: int) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'Delete From Gyms where GymID={};'.format(GymID)
    print(query)
    conn.execute(query)
    conn.close()


#Physical Data:
'''
CREATE TABLE PhysicalData (
    Username VARCHAR(50), 
    LastMuscleGroup VARCHAR(50), 
    Injury VARCHAR(50), 
    LastRecorded VARCHAR(50), 
    WorkSplit VARCHAR(50),
    PRIMARY KEY(Username)
);
'''
#Insert Row
def insertNewPhysicalData(Username: str, LastMuscleGroup: str, Injury: str, LastRecorded: str, WorkSplit: str):
    conn = db.connect()
    query = 'Insert Into PhysicalData (Username, LastMuscleGroup, Injury, LastRecorded, WorkSplit) VALUES ("{}", "{}", "{}", "{}", "{}");'.format(Username, LastMuscleGroup, Injury, LastRecorded, WorkSplit)
    conn.execute(query)
    conn.close()

#Search by username
def fetchPhysicalData(Username: str, LMG: str) -> dict:
    conn = db.connect()
    statement = 'SELECT LastMuscleGroup, Injury, LastRecorded, WorkSplit FROM PhysicalData WHERE Username = "{0}" AND LastMuscleGroup LIKE "%{1}%" ;'.format(Username, LMG)
    query = text(statement)
    print(query)
    query_results = conn.execute(query).fetchall() #Check to make sure this returns correctly
    #print(query_results[0])
    physicalData_list = []
    for result in query_results:
        item = {
            "LastMuscleGroup": result[0],
            "Injury": result[1],
            "LastRecorded": result[2],
            "WorkSplit": result[3]
        }
        physicalData_list.append(item)
    conn.close()
    return physicalData_list

#update by username
def updatePhysicalDataLastMuscleGroup(Username: int, text: str) -> None:
    conn = db.connect()
    query = 'Update PhysicalData set LastMuscleGroup = "{}" where Username = "{}";'.format(text, Username)
    conn.execute(query)
    conn.close()

def updatePhysicalDataInjury(Username: int, text: str) -> None:
    conn = db.connect()
    query = 'Update PhysicalData set Injury = "{}" where Username = "{}";'.format(text, Username)
    conn.execute(query)
    conn.close()

def updatePhysicalDataLastRecorded(Username: int, text: str) -> None:
    conn = db.connect()
    query = 'Update PhysicalData set LastRecorded = "{}" where Username = "{}";'.format(text, Username)
    conn.execute(query)
    conn.close()

def updatePhysicalDataWorkSplit(Username: int, text: str) -> None:
    conn = db.connect()
    query = 'Update PhysicalData set WorkSplit = "{}" where Username = "{}";'.format(text, Username)
    conn.execute(query)
    conn.close()


#Delete by username
def removePhysicalDataByUsername(Username: str) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'Delete From PhysicalData where Username="{}";'.format(Username)
    conn.execute(query)
    conn.close()

#Advanced Query
def getAvailibleReservations(Username: str) -> dict:
    conn = db.connect()
    print(Username)
    if len(Username) > 0:
        statement = 'SELECT ReservationID, GymName, StartTime, EndTime, Day, Month, Year \
            FROM Reservations r JOIN Gyms g USING (GymID) WHERE GymID IN \
            (SELECT GymID FROM Users u JOIN Gyms g USING(University) WHERE Username = "{}") \
            AND r.Username IS NULL ORDER BY Day DESC, StartTime DESC;'.format(Username)
    query = text(statement)
    print(query)
    query_results = conn.execute(query).fetchall()
    conn.close()
    reservations = []
    for result in query_results:
        item = {
            "ReservationID": result[0],
            "GymName": result[1],
            "StartTime": result[2],
            "EndTime": result[3],
            "Day": result[4],
            "Month": result[5],
            "Year": result[6],
        }
        reservations.append(item)
    
    return reservations

def update_reservation(username: str, ID: int) -> None:
    conn = db.connect()
    query = 'Update Reservations set Username = "{0}" where ReservationID = {1};'.format(username, ID)
    conn.execute(query)
    conn.close()

def fetch_my_reservations(username: str) -> dict:
    conn = db.connect()
    query = 'SELECT GymName, StartTime, EndTime, Day, Month, Year, ReservationID FROM Reservations NATURAL JOIN Gyms WHERE Username = "{0}";'.format(username)
    print(query)
    query_results = conn.execute(query).fetchall()
    conn.close()
    progress_list = []
    for result in query_results:
        item = {
            "GymName": result[0],
            "StartTime": result[1],
            "EndTime": result[2],
            "Day": result[3],
            "Month": result[4],
            "Year": result[5],
            "ReservationID": result[6]
        }
        progress_list.append(item)
    return progress_list

def cancel_reservation(ID: int) -> None:
    conn = db.connect()
    query = 'Update Reservations set Username = NULL where ReservationID = {0};'.format(ID)
    conn.execute(query)
    conn.close()
#Progress:

def fetch_progress(exercise: str, username: str) -> dict:
    conn = db.connect()
    statement = 'SELECT ProgressID, Exercise, Set_Size, Exercise_Stat FROM Progress WHERE Exercise LIKE "%{0}%" AND Username = "%{1}%" ORDER BY Exercise ASC;'.format(exercise, username)
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


def fetch_progmax(exercise: str, username: str) -> dict:
    conn = db.connect()
    if len(exercise) > 0:
        statement = 'SELECT Exercise, MAX(Set_Size) From Users Natural Join Progress WHERE Exercise LIKE "%{0}%" AND Username = "{1}" GROUP BY Exercise'.format(exercise, username)
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

# Users 

def update_user_name(email: str, text: str) -> None:
    conn = db.connect()
    query = 'Update Users set Username = "{1}" where Username = "{0}";'.format(text, email)
    conn.execute(query)
    conn.close()

def update_user_uni(email: str, text: str) -> None:
    conn = db.connect()
    query = 'Update Users set University = "{1}" where Username = "{0}";'.format(text, email)
    conn.execute(query)
    conn.close()

def update_user_fname(email: str, text: str) -> None:
    conn = db.connect()
    query = 'Update Users set Firstname = "{1}" where Username = "{0}";'.format(text, email)
    conn.execute(query)
    conn.close()

def update_user_lname(email: str, text: str) -> None:
    conn = db.connect()
    query = 'Update Users set Lastname = "{1}" where Username = "{0}";'.format(text, email)
    conn.execute(query)
    conn.close()

def update_user_password(email: str, text: str) -> None:
    conn = db.connect()
    query = 'Update Users set Password = "{1}" where Username = "{0}";'.format(text, email)
    conn.execute(query)
    conn.close()

def update_user_covidstatus(email: str, text: str) -> None:
    conn = db.connect()
    query = 'Update Users set CovidStatus = "{1}" where Username = "{0}";'.format(text, email)
    conn.execute(query)
    conn.close()

def insert_new_user(FirstName: str, LastName: str, Email: str, University: str, Username: str, Password: str, CovidStatus: str):
    conn = db.connect()
    query = 'Insert Into Users (FirstName, LastName, Email, University, Username, Password, CovidStatus) VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}");'.format(FirstName, LastName, Email, University, Username, Password, CovidStatus)
    conn.execute(query)
    query2 = 'Insert Into PhysicalData (Username, LastMuscleGroup, Injury, LastRecorded, WorkSplit) VALUES ("{}", "N/A", "N/A", "N/A", "N/A")'.format(Username)
    conn.execute(query2)
    conn.close()

def remove_user_by_email(Email: str) -> None:
    conn = db.connect()
    query = 'Delete From Users where Username="{}";'.format(Email)
    conn.execute(query)
    conn.close()

def fetch_users(username: str, university: str) -> dict:
    conn = db.connect()
    if len(username) > 0 and len(university) > 0:
        statement = 'SELECT * FROM Users WHERE Username LIKE "%{0}%" AND University LIKE "%{1}%" ORDER BY Username DESC, University ASC;'.format(username, university)
    elif len(username) > 0:
        statement = 'SELECT * FROM Users WHERE Username LIKE "%{0}%" ORDER BY Username DESC, University ASC;'.format(username)
    elif len(university) > 0:
        statement = 'SELECT * FROM Users WHERE University LIKE "%{0}%" ORDER BY University ASC, Username DESC;'.format(university)
    else:
        statement = 'SELECT * FROM Users ORDER BY Username DESC, University ASC;'
    query = text(statement)
    print(query)
    query_results = conn.execute(query).fetchall()
    conn.close()
    users_list = []
    for result in query_results:
        item = {
            "FirstName": result[0],
            "LastName": result[1],
            "Email": result[2],
            "University": result[3],
            "Username": result[4],
            "Password": result[5],
            "CovidStatus": result[6],
        }
        users_list.append(item)
    return users_list
	
def fetch_lift_records(exercise: str) -> dict:
    conn = db.connect()
    if len(exercise) > 0:
        statement = 'CREATE VIEW userMaxes as \
            SELECT DISTINCT pr.Username, u.University, pr.Exercise, MAX(tempUser.Exercise_Stat) as maxUser \
            FROM Progress pr NATURAL JOIN Users u, (SELECT p.Username, p.Exercise_Stat FROM Progress p WHERE p.Exercise = "{0}") as tempUser \
            WHERE pr.Exercise = "{0}" and pr.Username = tempUser.Username GROUP BY pr.Username, u.University;\n \
            SELECT DISTINCT u.University, um.Exercise, MAX(um.maxUser) as maxExercise \
            FROM userMaxes um LEFT JOIN Users u USING(Username) \
            GROUP BY u.University, um.Exercise \
            ORDER BY maxExercise DESC LIMIT 15\n \
            DROP VIEW IF EXISTS userMaxes'.format(exercise) 
    query = text(statement)
    print(query)
    conn.execute(query)
    query_results = conn.execute(query).fetchall()
    conn.close()
    lift_list = []
    for result in query_results:
        item = {
            "University": result[0],
            "Exercise": result[1],
            "Record": result[2]
        }
        lift_list.append(item)
    return lift_list