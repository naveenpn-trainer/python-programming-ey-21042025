import data_generator
from custom_objects import User
def main():
    users = data_generator.get_users()
    for user in users:
        print(f"User name: {user.name}")

if __name__ == '__main__':
    main()