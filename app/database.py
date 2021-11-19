import psycopg2
from psycopg2.extras import RealDictCursor
import time


#Databaseconnection

while True:

    try :
        conn = psycopg2.connect(host = 'localhost',database = 'fastapi',user = 'postgres',password= 'Lumosity@2',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection succesfull")
        break

    except Exception as error:
        print("Connection failed")
        print("Error: ",error)
        time.sleep(2)



