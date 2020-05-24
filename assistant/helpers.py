import hashlib
import os

def set_userdata(username, password, app_id):
    with open('../profiles/user.txt', 'a') as user_file:
        user_file.write('{}\n'.format(username))
        user_file.write('{}\n'.format(hash_password(password).hexdigest()))
        user_file.write('{}\n'.format(app_id))

def get_userdata():
    with open('../profiles/user.txt', 'r') as user_file:
        data = tup(user_file.readlines())
        user_file.close()
    return data

def get_userdata(app, username, password):
    with open('../profiles/user.txt', 'r') as user_file:
        hashed_pass = helpers.hash_password(password).hexdigest()
        if user_file.readline() != username:
            app.errorBox("Error", "Invalid Username\n Closing program")
            app.stop()
        elif user_file.readline() != hashed_pass:
            app.errorBox("Error", "Invalid Password\n Closing program")
            app.stop()
