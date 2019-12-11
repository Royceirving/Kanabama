import psycopg2

try:
    conn = psycopg2.connect(user="admin",
        password ="password",
        host="127.0.0.1",
        port="5432",
        database="postgres")
except BaseException as e:
    print(e)
    print("Cant open connection")
    exit(1)

cursor = conn.cursor()



def paste(val):
    query = "INSERT INTO info (id,name,description,priority,due_date) \n VALUES ({},'{}','{}',{},'{}')".format(val,"short story name","A short story description",2,"07-30-1998")
    print(query)
    cursor.execute(query)
    conn.commit()
    
def go():
    cursor.execute("SELECT * FROM info")
    resp = cursor.fetchall()
    print(resp)