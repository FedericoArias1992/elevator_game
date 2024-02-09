import time
import random
from datetime import datetime, timedelta
import sqlite3

class Elevator:
    def __init__(self, status, floor, moment=None, db_file='elevator.db'):
        self.status = status
        self.moment = moment or datetime.now()
        self.floor = floor
        #We initialize the database for storing elevator's data:
        self.conn = sqlite3.connect(db_file)
        self.c = self.conn.cursor()
        self._create_table_if_not()

    def _create_table_if_not(self):
        """Method for creating the database for storing"""
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS elevator (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                status TEXT NOT NULL,
                floor INTEGER NOT NULL,
                moment TIMESTAMP NOT NULL
            )
        ''')
        self.conn.commit()

    def demand(self, floor, moment=None):
        self.moment = moment or datetime.now()
        self.status = 'moving'
        self.c.execute('''
            INSERT INTO elevator (moment, floor, status)
            VALUES (?, ? ,?)
        ''', (self.moment, self.floor, self.status))
        self.conn.commit()

    def arrive(self, floor, moment=None):
        self.moment = moment or datetime.now()
        self.status = 'static'
        self.floor = floor
        self.c.execute('''
            INSERT INTO elevator (moment, floor, status)
            VALUES (?, ?, ?)
        ''', (self.moment, self.floor, self.status))
        self.conn.commit()

    def get_all_elevator_data(self):
        self.c.execute("SELECT * from elevator")
        data = self.c.fetchall()
        return data

    def close_conn(self):
        """Close connection when needed"""
        self.conn.close()
        return 'Connection closed Successfully!'

if __name__=='__main__':
    elevator = Elevator('static', 5) #initial position
    i =0
    # Establecer la semilla para el generador de números aleatorios
    random.seed(42)  
    #We will simulate 1000 uses of the elevator 
    while i < 200:
        random_number = random.randint(0, 9) #Generate random number for demand of next floor
        #print(i, f' elevator floor= {elevator.floor}  |  random_number= {random_number} ')
        if random_number != elevator.floor:
            if elevator.moment.hour > 6 and  elevator.moment.hour < 24:
                time_delta = timedelta(minutes=random.uniform(5, 15))   #Uniforme entre 5 y 15 min para horarios de dia
            else:
                time_delta = timedelta(minutes=random.uniform(35, 125))   #Uniforme entre 35 y 125 para horario noche
            elevator.demand(floor = random_number, moment = (time_delta + elevator.moment))
            #print(elevator.status, elevator.moment, elevator.floor)
            time_delta = timedelta(minutes=4)   #Suppose it takes 4 minutes until arriving next floor
            elevator.arrive(floor=random_number, moment = (time_delta + elevator.moment))
            #Una vez llega, lo movemos al piso que dice el machine learning que es el mejor para el reposo:
            elevator.demand(floor = 6, moment = (time_delta + elevator.moment))
            time_delta = timedelta(minutes=4)
            elevator.arrive(floor=6, moment = (time_delta + elevator.moment))
            i+=1
        
