from repository import JSONUserRepository
from auth_service import JSONAuthService
from user import User

repo = JSONUserRepository(file_path="repo/demo.json")
auth_service = JSONAuthService(repo=repo, auth_file_path="repo/auth_file.json")


def not_authorized_state() -> bool:
    print("Choose action: [1] - Sign in, [2] - Sign up, [3] - Exit")
    action = input()
    if action == "1":
        sign_in_action()
        return True
    elif action == "2":
        sign_up_action()
        return True
    elif action == "3":
        print("Exiting program")
        return False
    else:
        print("Please, enter valid action")
        return True

def sign_in_action():
    print("Signing in")
    login = input("Login: ")
    password = input("Password: ")
    if auth_service.sign_in(login, password):
        print(f"Succesfully signed in, {auth_service.current_user.name}")
    else:
        print("Failed to sign in")

def sign_up_action():
    print("Signing up")
    id_manual = int(input("ID (Placeholder, this part should be automated):"))
    name = input("Name: ")
    login = input("Login: ")
    password = input("Password: ")
    repo.add(User(id_manual, login, password, name))
    auth_service.sign_in(login, password) # Automatically signing in after signing up
    print(f"Succesfully signed up, {auth_service.current_user.name}")

def authorized_state() -> bool:
    print("Current profile:")
    print(f"Name: {auth_service.current_user.name}")
    print(f"Email: {auth_service.current_user.email}")
    print(f"Address: {auth_service.current_user.address}")
    print("Choose action: [1] - Change name, [2] - Change email, [3] - Change address")
    print("[4] - Change password, [5] - Sign out, [6] - Delete user, [7] - Exit")
    action = input()
    if action == '1':
        new_name = input("New name: ")
        auth_service.current_user.name = new_name
        repo.update(auth_service.current_user)
        print("Name successfully changed")
        return True
    elif action == '2':
        new_email = input("New email: ")
        auth_service.current_user.email = new_email
        repo.update(auth_service.current_user)
        print("Email successfully changed")
        return True
    elif action == '3':
        new_address = input("New name: ")
        auth_service.current_user.address = new_address
        repo.update(auth_service.current_user)
        print("Address successfully changed")
        return True
    elif action == '4':
        new_password = input("New password: ")
        auth_service.current_user.password = new_password
        repo.update(auth_service.current_user)
        print("Password successfully changed")
        return True
    elif action == '5':
        auth_service.sign_out()
        print("Signed out")
        return True
    elif action == '6':
        print("Are you sure? [Y] - Yes")
        action = input()
        if action == 'Y':
            deleting = auth_service.current_user
            auth_service.sign_out()
            repo.delete(deleting)
            print("User successfully deleted")
        else:
            print("Canceling deletion")
        return True
    elif action == '7':
        print("Exiting program")
        return False
    else:
        print("Please, enter valid action")
        return True


# Example User: User(0, "admin", "secret", "Administrator", "admin@stud.kantiana.com")

if auth_service.is_authorized:
    print(f"{auth_service.current_user.name} logged in automatically")

while True:
    if auth_service.is_authorized:
        if not authorized_state():
            break
    else:
        if not not_authorized_state():
            break