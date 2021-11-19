from typing import Optional

from starlette.requests import Request
import Services
from  Services import discount_generator
from fastapi import FastAPI,Form
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from psycopg2.extensions import AsIs


#Databaseconnection

while True:

    try :
        conn = psycopg2.connect(host = 'localhost',database = 'fastapi',user = 'postgres',password= 'Lumosity@24',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection succesfull")
        break

    except Exception as error:
        print("Connection failed")
        print("Error: ",error)
        time.sleep(2)


#FastAPI instance
app = FastAPI()

# Endpoint for generating discount codes
@app.post("/discount_code/")
async def generate_discount(count: int = Form(...), brand_name: str = Form(...)):
    print(count,brand_name) 
    discounts = []
    for i in range(count): 
       discounts.append(discount_generator())
    print(discounts)
    brands = 'update "Brands" SET discount_codes = %s where brand_name = %s'
    cursor.execute(brands,(discounts,brand_name),)
    conn.commit()        

#Endpoint to retrieve the code    
@app.get("/show_discounts/")
async def display_discount(brand_name: str = Form(...)):
    print(brand_name)
    user = 'select * from "Brands" where brand_name = %s'
    test = (brand_name,)
    cursor.execute(user,[test],)
    return cursor.fetchall()[0]['discount_codes'][0]











