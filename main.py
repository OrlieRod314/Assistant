from appJar import gui
import assistant.helpers

def start_buttons(name):
    if name == "Cancel":
        app.stop()
    elif name == "Reset":
        app.clearEntry("Username")
        app.clearEntry("Password")
        app.setFocus("Username")
    elif name == "Log In":
        username = app.getEntry("Username")
        password = app.getEntry("Password")

        input_data = (username.strip(), password)
        real_data = helpers.get_userdata()

        if input_data(0) != real_data(0):
            app.errorBox("Error", "Invalid Username\n Closing program")
            app.stop()
        elif input_data(1) != real_data(1):
            app.errorBox("Error", "Invalid Password\n Closing program")
            app.stop()
        else:
            app.removeAllWidgets()
            run_assistant(app)

def setup_buttons(name):
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

            helpers.set_userdata(username, password, app_id)

            app.infoBox("Setup Finished", "Setup Finished\nClosing program.\nRestart and log in with new credentials")
            app.stop()

def setup():
    app.removeAllWidgets()
    app.setTitle("Orlier Assistant First Time Setup")
    app.addLabel("Title", "Setup Page")

    app.addLabelEntry("Username")
    app.addSecretLabelEntry("Password")
    app.addSecretLabelEntry("Password again")
    app.addLabelEntry("Wolfram App ID")
    app.setFocus("Username")

    app.button('Accessibility', app.showAccess, icon='ACCESS')

    app.addButtons(["Submit", "Reset", "Cancel"], setup_buttons)

#def run_assistant(app):

def main():
    with gui("Orlier Assistant Login", "400x200", bg='orange', showIcon = False) as app:
        app.setIcon('img/half-life-icon.png')

        app.setResizable(False)
        app.addLabel("Title", "Login Page")

        app.addLabelEntry("Username")
        app.addSecretLabelEntry("Password")
        app.setFocus("Username")

        app.button('Accessibility', app.showAccess, icon='ACCESS')

        app.addButtons(["Log in", "Reset", "Cancel"], start_buttons)
        app.addButton("Set Up", setup)
        app.go()

if __name__ == "__main__":
    main()
