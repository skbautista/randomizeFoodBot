import sqlite3

class database:
    #Initial construct of the database
    def __init__(self, fileName):
        self.con = sqlite3.connect(fileName)
        self.cur = self.con.cursor()
        try:
            self.cur.execute("CREATE TABLE food(name VARCHAR UNIQUE, restaurant_type VARCHAR)")
        except:
            pass
        
    #Executes a query to add a restaurant in the database
    def addFood(self, name: str, rType: str):
        try:
            self.cur.execute(f"INSERT INTO food VALUES(?, ?)", [name.lower(), rType.lower()])
            self.con.commit()
        except:
            pass

    #returns a set from a query to get all of the restaurant types in the database and
    def getAllTypes(self):
        return {x[0] for x in self.cur.execute("SELECT restaurant_type FROM food").fetchall()}
    
    #Returns a list from a query to get all of the restaurants and/or depending on the restaurant type
    def getAllFood(self, restaurantType: str | None):            
        if restaurantType == None:
            query = "SELECT name FROM food"
        else:
            query = f"SELECT name FROM food WHERE restaurant_type='{restaurantType.lower()}'"

        return [x[0] for x in self.cur.execute(query).fetchall()]

              
db1 = database("Food.db")
# db1.addFood("Fuh Station", "Asian")
# db1.addFood("New Island", "Asian")
# db1.addFood("Earls", "Western")
# db1.addFood("Olive Garden", "Italian")
# print(db1.getAllTypes())
