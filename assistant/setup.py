import hashlib
import os
from appJar import gui

if os.path.exists("../profiles/user.txt"):
    os.remove("../profiles/user.txt")

def hash_password(password):
    password = hashlib.md5(password.encode())
    return password

def main():
    def press(name):
        if name == "Cancel":
            app.stop()
        elif name == "Reset":
            app.clearEntry("Username")
            app.clearEntry("Password")
            app.clearEntry("Password again")
            app.clearEntry("Wolfram App ID")
            app.setFocus("Username")
        elif name == "Submit":
            username = app.getEntry("Username")
            if app.getEntry("Password") != app.getEntry("Password again"):
                app.errorBox("Error", "Invalid Password\n Closing program")
                app.stop()
            else:
                password = app.getEntry("Password")
                app_id = app.getEntry("Wolfram App ID")

                with open('../profiles/user.txt', 'a') as user_file:
                    user_file.write('{}\n'.format(username))
                    user_file.write('{}\n'.format(hash_password(password).hexdigest()))
                    user_file.write('{}\n'.format(app_id))
                app.stop()

    with gui("Orlier Assistant Setup", "400x200", bg='orange', showIcon = False) as app:
        app.setIcon('../img/half-life-icon.png')

        app.setResizable(False)
        app.addLabel("Title", "Setup Page")

        app.addLabelEntry("Username")
        app.addSecretLabelEntry("Password")
        app.addSecretLabelEntry("Password again")
        app.addLabelEntry("Wolfram App ID")
        app.setFocus("Username")

        app.button('Accessibility', app.showAccess, icon='ACCESS')

        app.addButtons(["Submit", "Reset", "Cancel"], press)
        app.go()

if __name__ == "__main__":
    main()
