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

def update_user_name(email: str, text: str) -> None:
    conn = db.connect()
    query = 'Update Users set Username = "{1}" where Email = {0};'.format(text, email)
    conn.execute(query)
    conn.close()

def update_user_uni(email: str, text: str) -> None:
    conn = db.connect()
    query = 'Update Users set University = "{1}" where Email = {0};'.format(text, email)
    conn.execute(query)
    conn.close()

def update_user_fname(email: str, text: str) -> None:
    conn = db.connect()
    query = 'Update Users set Firstname = "{1}" where Email = {0};'.format(text, email)
    conn.execute(query)
    conn.close()

def update_user_lname(email: str, text: str) -> None:
    conn = db.connect()
    query = 'Update Users set Lastname = "{1}" where Email = {0};'.format(text, email)
    conn.execute(query)
    conn.close()

def update_user_password(email: str, text: str) -> None:
    conn = db.connect()
    query = 'Update Users set Password = "{1}" where Email = {0};'.format(text, email)
    conn.execute(query)
    conn.close()

def update_user_covidstatus(email: str, text: str) -> None:
    conn = db.connect()
    query = 'Update Users set CovidStatus = "{1}" where Email = {0};'.format(text, email)
    conn.execute(query)
    conn.close()

def insert_new_user(FirstName: str, LastName: str, Email: str, University: str, Username: str, Password: str, CovidStatus: str):
    conn = db.connect()
    query = 'Insert Into Users (FirstName, LastName, Email, University, Username, Password, CovidStatus) VALUES ("{}", "{}", "{}", "{}");'.format(FirstName, LastName, Email, University, Username, Password, CovidStatus)
    conn.execute(query)
    conn.close()

def remove_user_by_email(Email: str) -> None:
    conn = db.connect()
    query = 'Delete From Users where Email={};'.format(Email)
    conn.execute(query)
    conn.close()

def fetch_users(username: str, university: str) -> dict:
    conn = db.connect()
    if len(username) > 0 and len(university) > 0:
        statement = 'SELECT Email, University, Username, CovidStatus FROM Users WHERE Username LIKE "%{0}%" AND University LIKE "%{1}%" ORDER BY Username DESC, University ASC;'.format(username, university)
    elif len(username) > 0:
        statement = 'SELECT Email, University, Username, CovidStatus FROM Users WHERE Username LIKE "%{0}%" ORDER BY Username DESC, University ASC;'.format(username)
    elif len(university) > 0:
        statement = 'SELECT Email, University, Username, CovidStatus FROM Users WHERE University LIKE "%{0}%" ORDER BY University ASC, Username DESC;'.format(university)
    else:
        statement = 'SELECT Email, University, Username, CovidStatus FROM Users ORDER BY Username DESC, University ASC;'
    query = text(statement)
    print(query)
    query_results = conn.execute(query).fetchall()
    conn.close()
    users_list = []
    for result in query_results:
        item = {
            "First Name": result[0],
            "Last Name": result[1],
            "Email": result[2],
            "University": result[3],
            "Username": result[4],
            "Password": result[5],
            "Covid Status": result[6],
        }
        users_list.append(item)
    return users_list
	