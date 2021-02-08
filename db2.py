from mysql.connector import connect, Error, cursor


create_db_query = "CREATE DATABASE  IF NOT EXISTS moviesdb"
create_table_query  = """
CREATE TABLE  IF NOT EXISTS movies(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    release_year YEAR(4),
    genre VARCHAR(100),
    instock INT
)
"""

with connect(host="localhost",
    user="root",
    password="hejsan123"
) as connection:
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)
        

with connect(host="localhost",
    user="root",
    password="hejsan123",
    database="moviesdb"
) as connection:
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)
        connection.commit()        
        cursor.execute("select * from movies where title='Miami supercops'")
        results = cursor.fetchall()
        if len(results) == 0:
            cursor.execute(''' INSERT INTO movies(title,release_year,genre,instock) VALUES(%s,%s,%s,%s)''',('Miami supercops',1985,'Drama',3))
            connection.commit()        
