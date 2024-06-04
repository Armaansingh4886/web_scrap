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

        # dbname="your_db_name",
        # user="your_username",
        # password="your_password",
        # host="your_host",
        # port="your_port"
    )

    # Create a cursor object using the cursor() method
    cursor = conn.cursor()

    # Execute your SQL query
    cursor.execute("SELECT * FROM properties")

    # Fetch all the rows using fetchall() method
    rows = cursor.fetchall()

    

  # Define the folder path where you want to save the CSV file
    folder_path = "./exports"

    # Ensure that the folder exists, if not create it
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    except OSError as e:
        print(f"Error creating directory: {e}")
        return

    # Define the CSV file name
    csv_file = os.path.join(folder_path, "output.csv")

    # Define the CSV file name
    # csv_file = "output.csv"

    # Write data to CSV file
    with open(csv_file, 'w', newline='') as file:
    
        writer = csv.writer(file)

        # Write header
        writer.writerow([i[0] for i in cursor.description])

        # Write rows
        writer.writerows(rows)

        # Write footer
        # For example, you could write total number of rows
        writer.writerow(["Total Rows:", len(rows)])

    # Close the cursor and connection
    cursor.close()
    conn.close()

    print("CSV file exported successfully.")

# Call the function to export data to CSV
export_to_csv()