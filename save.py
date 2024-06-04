
import psycopg2


# DATABASE DETAILS
hostname="localhost"
database="scrape"
username="postgres"
pwd="12345"
port_id=5432


def save(data):
    try:


        # CONNECTING DAGTABASE
        conn= psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
        )
# CREATING TABLE IN DATABASE
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS properties')
        create_table='''CREATE TABLE IF NOT EXISTS properties(
                        id              SERIAL PRIMARY KEY,
                        rank            varchar(200),
                        name            varchar(200) ,
                        industry        varchar(200),
                        revenue         varchar(200),
                        headquarters    varchar(200)        )'''
        cur.execute(create_table)
    # INSERTING DATA TO DATABASE
        insert_data = 'INSERT INTO properties (rank,name,industry,revenue,headquarters) VALUES (%s,%s,%s,%s,%s)'
        for item in data:
            print(item)
            insert_values=item
            cur.execute(insert_data,insert_values)
        conn.commit()
        print("added succesfully")

    except Exception as error:
        print(error)


