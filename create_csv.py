import psycopg2
import csv
import os


def export_to_csv():
    # Connect to your PostgreSQL database
    conn = psycopg2.connect(
    host="localhost",
    dbname="scrape",
    user="postgres",
    password="12345",
    port="5432"

       
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM companies")

    rows = cursor.fetchall()
    
    

  # Define the folder path where you want to save the CSV file
    folder_path = "./exports"

    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    except OSError as e:
        print(f"Error creating directory: {e}")
        return

    csv_file = os.path.join(folder_path, "output.csv")

    # Write data to CSV file
    with open(csv_file, 'w', newline='') as file:
    
        writer = csv.writer(file)
        # print(cursor.description)
        # Write header
        writer.writerow([i[0] for i in cursor.description])

        # Write rows
        writer.writerows(rows)

     
        writer.writerow(["Total Rows:", len(rows)])


    cursor.close()
    conn.close()

    print("CSV file exported successfully.")

export_to_csv()