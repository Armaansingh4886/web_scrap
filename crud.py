
import psycopg2


# DATABASE DETAILS
hostname="localhost"
database="scrape"
username="postgres"
pwd="12345"
port_id=5432

conn= psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
        )
cur = conn.cursor()
def insert(data):
    try:
        
    # INSERTING DATA TO DATABASE
        insert_data = 'INSERT INTO companies (rank,name,industry,revenue,headquarters) VALUES (%s,%s,%s,%s,%s)'
        insert_values=data
        cur.execute(insert_data,insert_values)
        conn.commit()
        print("added succesfully")

    except Exception as error:
        print(error)

def delete(data):
    select_query = """SELECT * FROM companies WHERE rank = %s and name = %s"""

   

    # Execute the SELECT statement
    cur.execute(select_query, (data))

    # Fetch the row
    row = cur.fetchone()

    if row:
        delete_data='DELETE FROM companies WHERE rank = %s and name = %s'
        cur.execute(delete_data,(data))
        conn.commit()
        print("Row deleted successfully")
    else:
        print("No rows found matching the condition.")

   

def update(data):




    select_query = """SELECT * FROM companies WHERE rank = %s and name = %s"""

   

    # Execute the SELECT statement
    cur.execute(select_query, (data[5],data[6]))
    print(data[5],data[6])
    # Fetch the row
    row = cur.fetchone()

    if row:
        for i in range(1,4):
            if(data[i]==""):
                data[i]=row[i+1]
        print(row)
        update_query = """UPDATE companies  
                      SET rank = %s, name = %s,industry=%s,revenue=%s,headquarters=%s
                      WHERE rank = %s and name = %s"""

   
            # Execute the UPDATE statement
        cur.execute(update_query, (data))
        conn.commit()
        print("Row updated successfully")
    else:
        print("No rows found matching the condition.")
    