import tkinter as tk
from tkinter import messagebox
from getpass import getpass
import re

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

class DatabaseManager:
    def __init__(self, connection_url):
        self.connection_url = connection_url
        self.engine = create_engine(connection_url, pool_pre_ping=True)
        self.metadata = MetaData(bind=self.engine, reflect=True)

    def clear_database(self):
        self.metadata.drop_all()

    def create_database(self, database_name):
        self.engine.execution_options(isolation_level="AUTOCOMMIT").execute(f"CREATE DATABASE {database_name}")

    def reset_database(self):
        self.clear_database()
        self.create_database("game")

    def connect_to_database(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def get_active_connections(self):
        return self.engine.execute("SELECT * FROM pg_stat_activity").fetchall()

class User:
    def __init__(self):
        self.token = {}

    def update_token(self, username, password, host, port, database, isAdmin, connection_url):
        self.token = {
            'username': username,
            'password': password,
            'host': host,
            'port': port,
            'database': database,
            'admin': isAdmin,
            'connection_url': connection_url
        }

    def clear_token(self):
        self.token = {}

    def is_logged_in(self):
        return bool(self.token)

    def is_logged_off(self):
        return not bool(self.token)

    def is_admin(self):
        return self.token.get('admin', False)

def validate_connection_url(connection_url):
    # Validate the connection URL format
    url_pattern = r"postgresql:\/\/(\w+):(\w+)@([A-Za-z0-9\-\.]+):(\d+)\/(\w+)"
    match = re.match(url_pattern, connection_url)
    return match is not None

def log_in():
    global user

    if user.is_logged_off():
        # Prompt the user to enter PostgreSQL credentials
        login_window = tk.Toplevel(window)
        login_window.title("Log In")
        login_window.geometry("250x250")

        username_label = tk.Label(login_window, text="Username:")
        username_label.pack()
        username_entry = tk.Entry(login_window, width=30)
        username_entry.pack()

        password_label = tk.Label(login_window, text="Password:")
        password_label.pack()
        password_entry = tk.Entry(login_window, width=30, show="*")
        password_entry.pack()

        host_label = tk.Label(login_window, text="Host (default: 'localhost'):")
        host_label.pack()
        host_entry = tk.Entry(login_window, width=30)
        host_entry.pack()
        host_entry.insert(tk.END, "localhost")

        port_label = tk.Label(login_window, text="Port (default: '5432'):")
        port_label.pack()
        port_entry = tk.Entry(login_window, width=30)
        port_entry.pack()
        port_entry.insert(tk.END, "5432")

        database_label = tk.Label(login_window, text="Database (default: 'game'):")
        database_label.pack()
        database_entry = tk.Entry(login_window, width=30)
        database_entry.pack()
        database_entry.insert(tk.END, "game")

        def submit_login():
            global user
            username = username_entry.get().strip()
            password = password_entry.get().strip()
            host = host_entry.get().strip() or "localhost"
            port = port_entry.get().strip() or "5432"
            database = database_entry.get().strip() or "game"

            # Update the connection URL and check if the user is an admin
            connection_url = f"postgresql://{username}:{password}@{host}:{port}/{database}"
            if validate_connection_url(connection_url):
                user.update_token(username, password, host, port, database, (username == "admin"), connection_url)
                print("Sign in successful.")
                logged_status_button.configure(text="Log Out")
                login_window.destroy()
                update_connection_url()
            else:
                messagebox.showerror("Error", "Invalid connection URL format.")

        submit_button = tk.Button(login_window, text="Submit", command=submit_login)
        submit_button.pack()
    else:
        log_out()

def log_out():
    user.clear_token()
    logged_status_button.configure(text="Log In")
    update_connection_url()

def clear_database_gui():
    if user.is_logged_in():
        try:
            db_manager = DatabaseManager(user.token['connection_url'])
            db_manager.clear_database()
            print("Database cleared successfully.")
            messagebox.showinfo("Success", "Database cleared successfully.")
        except Exception as e:
            print("Error clearing database:", str(e))
            messagebox.showerror("Error", str(e))
    else:
        print("You must be logged in.")

def create_database_gui():
    if user.is_logged_in():
        database_window = tk.Toplevel(window)
        database_window.title("Enter Database Name")
        database_window.geometry("300x120")

        def submit_database_name():
            database_name = database_entry.get().strip()
            if database_name:
                try:
                    db_manager = DatabaseManager(user.token['connection_url'])
                    db_manager.create_database(database_name)
                    print("Database created successfully.")
                    messagebox.showinfo("Success", "Database created successfully.")
                    database_window.destroy()
                except Exception as e:
                    print("Error creating database:", str(e))
                    messagebox.showerror("Error", str(e))
            else:
                print("Database name is required.")

        database_label = tk.Label(database_window, text="Database Name:")
        database_label.pack()
        database_entry = tk.Entry(database_window, width=30)
        database_entry.pack()
        submit_button = tk.Button(database_window, text="Submit", command=submit_database_name)
        submit_button.pack()
    else:
        print("You must be logged in.")

def reset_database_gui():
    if user.is_logged_in():
        try:
            db_manager = DatabaseManager(user.token['connection_url'])
            db_manager.reset_database()
            print("Database reset successfully.")
            messagebox.showinfo("Success", "Database reset successfully.")
        except Exception as e:
            print("Error resetting database:", str(e))
            messagebox.showerror("Error", str(e))
    else:
        print("You must be logged in.")

def connect_to_database_gui():
    if user.is_logged_in():
        try:
            db_manager = DatabaseManager(user.token['connection_url'])
            session = db_manager.connect_to_database()
            print("Connected to database successfully.")
            session.close()
        except Exception as e:
            print("Error connecting to database:", str(e))
    else:
        print("You must be logged in.")

def get_active_connections_gui():
    if user.is_logged_in():
        try:
            db_manager = DatabaseManager(user.token['connection_url'])
            connections = db_manager.get_active_connections()
            print("Active Connections:")
            for connection in connections:
                print(connection)
        except Exception as e:
            print("Error retrieving active connections:", str(e))
    else:
        print("You must be logged in.")

def update_connection_url():
    global user, connection_url_text
    connection_url = user.token.get('connection_url', '')
    connection_url = connection_url.replace(f":{user.token.get('password')}", ":********")  # Hide password
    connection_url_text.set(connection_url)

def get_active_connections_gui():
    if user.is_logged_in():
        try:
            db_manager = DatabaseManager(user.token['connection_url'])
            connections = db_manager.get_active_connections()
            print("Active Connections:")
            for connection in connections:
                print(connection)
        except Exception as e:
            print("Error retrieving active connections:", str(e))
    else:
        print("You must be logged in.")

def clear_database_gui():
    if user.is_logged_in():
        try:
            db_manager = DatabaseManager(user.token['connection_url'])
            db_manager.clear_database()
            print("Database cleared successfully.")
            messagebox.showinfo("Success", "Database cleared successfully.")
        except Exception as e:
            print("Error clearing database:", str(e))
            messagebox.showerror("Error", str(e))
    else:
        print("You must be logged in.")

def create_database_gui():
    if user.is_logged_in():
        database_window = tk.Toplevel(window)
        database_window.title("Enter Database Name")
        database_window.geometry("300x120")

        def submit_database_name():
            database_name = database_entry.get().strip()
            if database_name:
                try:
                    db_manager = DatabaseManager(user.token['connection_url'])
                    db_manager.create_database(database_name)
                    print("Database created successfully.")
                    messagebox.showinfo("Success", "Database created successfully.")
                    database_window.destroy()
                except Exception as e:
                    print("Error creating database:", str(e))
                    messagebox.showerror("Error", str(e))
            else:
                print("Database name is required.")

        database_label = tk.Label(database_window, text="Database Name:")
        database_label.pack()
        database_entry = tk.Entry(database_window, width=30)
        database_entry.pack()
        submit_button = tk.Button(database_window, text="Submit", command=submit_database_name)
        submit_button.pack()
    else:
        print("You must be logged in.")

def reset_database_gui():
    if user.is_logged_in():
        try:
            db_manager = DatabaseManager(user.token['connection_url'])
            db_manager.reset_database()
            print("Database reset successfully.")
            messagebox.showinfo("Success", "Database reset successfully.")
        except Exception as e:
            print("Error resetting database:", str(e))
            messagebox.showerror("Error", str(e))
    else:
        print("You must be logged in.")

def connect_to_database_gui():
    if user.is_logged_in():
        try:
            db_manager = DatabaseManager(user.token['connection_url'])
            session = db_manager.connect_to_database()
            print("Connected to database successfully.")
            session.close()
        except Exception as e:
            print("Error connecting to database:", str(e))
    else:
        print("You must be logged in.")

def log_in():
    global user

    if user.is_logged_off():
        # Prompt the user to enter PostgreSQL credentials
        login_window = tk.Toplevel(window)
        login_window.title("Log In")
        login_window.geometry("250x250")

        username_label = tk.Label(login_window, text="Username:")
        username_label.pack()
        username_entry = tk.Entry(login_window, width=30)
        username_entry.pack()

        password_label = tk.Label(login_window, text="Password:")
        password_label.pack()
        password_entry = tk.Entry(login_window, width=30, show="*")
        password_entry.pack()

        host_label = tk.Label(login_window, text="Host (default: 'localhost'):")
        host_label.pack()
        host_entry = tk.Entry(login_window, width=30)
        host_entry.pack()
        host_entry.insert(tk.END, "localhost")

        port_label = tk.Label(login_window, text="Port (default: '5432'):")
        port_label.pack()
        port_entry = tk.Entry(login_window, width=30)
        port_entry.pack()
        port_entry.insert(tk.END, "5432")

        database_label = tk.Label(login_window, text="Database (default: 'game'):")
        database_label.pack()
        database_entry = tk.Entry(login_window, width=30)
        database_entry.pack()
        database_entry.insert(tk.END, "game")

        def submit_login():
            global user
            username = username_entry.get().strip()
            password = password_entry.get().strip()
            host = host_entry.get().strip() or "localhost"
            port = port_entry.get().strip() or "5432"
            database = database_entry.get().strip() or "game"

            # Update the connection URL and check if the user is an admin
            connection_url = f"postgresql://{username}:{password}@{host}:{port}/{database}"
            if validate_connection_url(connection_url):
                user.update_token(username, password, host, port, database, (username == "admin"), connection_url)
                print("Sign in successful.")
                logged_status_button.configure(text="Log Out")
                login_window.destroy()
                update_connection_url()
            else:
                messagebox.showerror("Error", "Invalid connection URL format.")

        submit_button = tk.Button(login_window, text="Submit", command=submit_login)
        submit_button.pack()
    else:
        log_out()

def log_out():
    user.clear_token()
    logged_status_button.configure(text="Log In")
    update_connection_url()

def validate_connection_url(connection_url):
    # Validate the connection URL format
    url_pattern = r"postgresql:\/\/(\w+):(\w+)@([A-Za-z0-9\-\.]+):(\d+)\/(\w+)"
    match = re.match(url_pattern, connection_url)
    return match is not None

window = tk.Tk()
window.title("Database Interface")
window.geometry("400x300")

connection_url_text = tk.StringVar()
connection_url_text.set("")

# Create an instance of the User class
user = User()

logged_status_button = tk.Button(window, text="Log In", command=log_in)
logged_status_button.pack()

clear_button = tk.Button(window, text="Clear Database", command=clear_database_gui)
clear_button.pack()

create_button = tk.Button(window, text="Create Database", command=create_database_gui)
create_button.pack()

reset_button = tk.Button(window, text="Reset Database", command=reset_database_gui)
reset_button.pack()

connect_button = tk.Button(window, text="Connect to Database", command=connect_to_database_gui)
connect_button.pack()

connections_button = tk.Button(window, text="Get Active Connections", command=get_active_connections_gui)
connections_button.pack()

url_text_label = tk.Label(window, text="Connection URL:")
url_text_label.pack()

connection_url_label = tk.Label(window, textvariable=connection_url_text)
connection_url_label.pack()

update_connection_url()

window.mainloop()