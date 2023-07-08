from models import User
import database

def main():
    database.initialize_database()

    # Create a new user
    new_user = User(name='John Doe', email='john.doe@example.com')
    database.add_user(new_user)

    # Query all users
    users = database.get_all_users()
    for user in users:
        print(user.name, user.email)

    # Update a user
    user = users[0]
    user.email = 'new-email@example.com'
    database.update_user(user)

    # Delete a user
    user = users[0]
    database.delete_user(user)

    database.close_session()

if __name__ == '__main__':
    main()
