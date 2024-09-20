import psycopg2

def connect_to_db():
    try:
        connection = psycopg2.connect(
            user='abdalla',
            password='Rayan101',
            host='localhost',
            port='5432',
            database='grocery_shop'
        )
        print("Connection successful!")
        return connection
    except Exception as e:
        print("Error connecting to database:", e)

if __name__ == "__main__":
    conn = connect_to_db()
    # Remember to close the connection when done
    if conn:
        conn.close()
