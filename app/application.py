from typing import Optional

from starlette.requests import Request
import Services
from  Services import discount_generator
from fastapi import FastAPI,Form
import psycopg2
from psycopg2.extras import RealDictCursor
import time


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


''' cursor.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
for table in cursor.fetchall():
    print(table)  '''

#cursor.execute("SELECT * FROM public.{}".format("Brands"))
''' cursor.execute('SELECT * FROM "Brands"')
row = cursor.fetchall()
while row is not None:
    print(row)  '''

''' store = "billogram"
test = 'select discount_codes FROM "Brands" WHERE brand_name = %s' 
cursor.execute(test,store,) '''

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "World!!!24"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

#count: int = Form(...), brand_name: str = Form(...)

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

@app.get("/show_discounts")
async def display_discount(brand_name: str = Form(...)):
    print(brand_name)
    user = 'select discount_codes from "Brands" where brand_name="billogram"'
    #print(user)
    #cursor.execute(user,(brand_name),)
    cursor.execute(user,)
    rows = cursor.fetchone()
    for row in rows:
        disc_result = row[0]
    print(disc_result)


