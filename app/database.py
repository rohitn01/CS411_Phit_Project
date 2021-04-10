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
def fetchPhysicalData(Username: str) -> dict:
    conn = db.connect()
    statement = 'SELECT LastMuscleGroup, Injury, LastRecorded, WorkSplit FROM PhysicalData WHERE Username LIKE "%{0}%" ;'.format(Username)
    query = text(statement)
    print(query)
    query_results = conn.execute(query).fetchall() #Check to make sure this returns correctly
    conn.close()
    return query_results

#update by username
def updatePhysicalDataLastMuscleGroup(Username: int, text: str) -> None:
    conn = db.connect()
    query = 'Update PhysicalData set LastMuscleGroup = "{}" where Username = {};'.format(text, Username)
    conn.execute(query)
    conn.close()

def updatePhysicalDataInjury(Username: int, text: str) -> None:
    conn = db.connect()
    query = 'Update PhysicalData set Injury = "{}" where Username = {};'.format(text, Username)
    conn.execute(query)
    conn.close()

def updatePhysicalDataLastRecorded(Username: int, text: str) -> None:
    conn = db.connect()
    query = 'Update PhysicalData set LastRecorded = "{}" where Username = {};'.format(text, Username)
    conn.execute(query)
    conn.close()

def updatePhysicalDataWorkSplit(Username: int, text: str) -> None:
    conn = db.connect()
    query = 'Update PhysicalData set WorkSplit = "{}" where Username = {};'.format(text, Username)
    conn.execute(query)
    conn.close()


#Delete by username
def removePhysicalDataByUsername(Username: str) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'Delete From PhysicalData where Username={};'.format(Username)
    conn.execute(query)
    conn.close()

#Advanced Query
def getAvailibleReservations(username: str) -> dict:
    conn = db.connect()
    if len(username) > 0:
        statement = 'SELECT ReservationID, GymName, StartTime, EndTime, Day, Month, Year \
            FROM Reservations r JOIN Gyms g USING (GymID) WHERE GymID IN \
            (SELECT GymID FROM Users u JOIN Gyms g USING(University) WHERE Username = "{}") \
            AND r.Username IS NULL ORDER BY Day DESC, StartTime DESC;'.format(username)
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


