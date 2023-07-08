import getpass
import psycopg2

def get_active_connections(username, password, host, port, database):
    try:
        conn = psycopg2.connect(user=username, password=password, host=host, port=port, database=database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pg_stat_activity WHERE datname = current_database()")
        connections = cursor.fetchall()
        cursor.close()
        conn.close()
        return connections
    except psycopg2.OperationalError as e:
        print("Error connecting to the database:", e)
        return []

def print_connection_url(username, password, host, port, database):
    connection_url = f"postgresql://{username}:{password}@{host}:{port}/{database}"
    print("Connection URL:", connection_url)

# Prompt the user to enter PostgreSQL credentials
username = input("Enter PostgreSQL username: ")
password = getpass.getpass("Enter PostgreSQL password: ")
host = "localhost"  # Replace with your PostgreSQL host if needed
port = 5432  # Replace with your PostgreSQL port if needed
database = input("Enter the name of the database: ")

# Print the connection URL
print_connection_url(username, password, host, port, database)

# Get the active connections
connections = get_active_connections(username, password, host, port, database)

# Print the active connections
print("Active Connections:")
for connection in connections:
    pid, database, user, client_addr, client_port = connection[0:5]
    print_connection_url(user, password, host, port, database)
