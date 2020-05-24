import hashlib
import os
from appJar import gui
import assistant.setup, assistant.assistant

# import assistant.setup as setup

def hash_password(password):
    password = hashlib.md5(password.encode())
    return password

def main():
    def press(name):
        if name == "Cancel":
            start.stop()
        elif name == "Reset":
            start.clearEntry("Username")
            start.clearEntry("Password")
            start.setFocus("Username")
        elif name == "Log In":
            username = start.getEntry("Username")
            password = start.getEntry("Password")
            with open('../profiles/user.txt', 'r') as user_file:
                hashed_pass = hash_password(password).hexdigest()
                if user_file.readline() != username:
                    start.errorBox("Error", "Invalid Username\n Closing program in 5 seconds")
                    start.stop()
                elif user_file.readline() != hashed_pass:
                    start.errorBox("Error", "Invalid Password\n Closing program in 5 seconds")
                    start.stop()
                else:
                    user_file.close()
                    assistant.assistant.main()
                    start.stop()

    # Do I need to add name as parameter? Run to find out
    def setup():
        assistant.setup.main()
        start.stop()

    with gui("Orlier Assistant Login", "400x200", bg='orange', showIcon = False) as start:
        start.setIcon('img/half-life-icon.png')

        start.setResizable(False)
        start.addLabel("Title", "Login Page")

        start.addLabelEntry("Username")
        start.addSecretLabelEntry("Password")
        start.setFocus("Username")

        start.button('Accessibility', start.showAccess, icon='ACCESS')

        start.addButtons(["Log in", "Reset", "Cancel"], press)
        start.addButton("Set Up", setup)
        start.go()

if __name__ == "__main__":
    main()
