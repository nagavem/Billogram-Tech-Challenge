# Billogram-Tech-Challenge

This is the repo containing Nagasudeep's solution to the coding challenge put forth by billogram. 
The application comprises of 2 endpoints for generation of discount codes and also for fetching the discount code assigned to a particular brand. 


## 1.User Guide and Setup

1. In case you havent already, [Install Python](https://www.python.org/downloads/).
2. You will need [PostgreSQL](https://www.postgresql.org/download/) for managing your data store create your schema here and below I will show some commands used for connecting and interacting with the table in python.
3. Install [Docker](https://docs.docker.com/get-docker/) to create an image for you
4. Clone this repo: `$ git clone  https://github.com/nagavem/Billogram-Tech-Challenge.git`
5. Install the dependencies: `$ pip install -r requirements.txt `
6. You can use swaggerUI at (http://127.0.0.1:8000/docs) but i recommend using [Postman](https://www.postman.com/downloads/) for API testing. 
7. Run the app server using the command : ` uvicorn application:app --reload`
8. The service is now exposed at (http://127.0.0.1:8000/) with the endpoints discount_code for discount generation and show_discounts for fetching the discount for a specific brand.

### Database

The database is hosted locally on postgreSQL and is a simple one comprising of the Brands table where the brand_name, brand id and the discount codes are stored.

The following code in apllication.py shows how database connection was established following which cursor was used in combination with python to write and execute queries in code.


:

```
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
```

**Query Examples**

```
'update "Brands" SET discount_codes = %s where brand_name = %s'
'select * from "Brands" where brand_name = %s'
```




## 2.Tools/Frameworks and Reasoning

**FastAPI**: 

FastAPI was chosen as the API framework due to its support of asynchronous code, ease of development which leads to great speed in implementation and makes it easy to test.


## 3.Limitations 

This section discusses the limitations brought about from time constraints. 




