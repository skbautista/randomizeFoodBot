import sqlite3

class database:
    def __init__(self, fileName):
        self.con = sqlite3.connect(fileName)
        self.cur = self.con.cursor()
        try:
            self.cur.execute("CREATE TABLE food(name UNIQUE)")
        except:
            pass

    def addFood(self, name):
        try:
            self.cur.execute(f"INSERT INTO food VALUES(?, ?)", [name, ])
            self.con.commit()
        except:
            pass
    
    def getAllFood(self):
        return self.cur.execute("SELECT name, FROM food").fetchall()
    
# db1 = database("Food.db")
# db1.addFood("fuh")
# db1.addFood("japabowl")  
# print(db1.getAllFood())
# db1.addFood("thien", "Asian")
# db1.addFood("japabowl", "Asian")
# db1.addFood("fuh", "Asian")
# print(db1.getFood("montanas"))
# print(db1.getAllFood())