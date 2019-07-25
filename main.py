from flask import Flask, request, redirect, render_template 
import cgi 
import os 


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html')

def is_valid_email(address):
    if len(address) < 3 or len(address) > 20:
        return False

    at = "@"
    at_count = address.count(at)
    if at_count != 1:
        return False
        
    dot = "."
    dot_count = address.count(dot)
    if dot_count != 1:
        return False
        
    space = " "
    space_count = address.count(space)
    if space_count != 0:
        return False

    else:
        return True


@app.route("/signup", methods = ['POST', 'GET'])
def signup():
    
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    
    
    username_error = ''
    password_error = '' 
    verify_error = '' 
    email_error = ''
    space = ' '

    if len(username) < 3 or len(username) > 20:
        username_error = 'username must be betweeen 3 and 20 characters'
        password = ''
        verify = ''
    if username.count(space) != 0:
        username_error = 'username cannot contain spaces'
        password = ''
        verify = ''
    
    if len(password) < 3 or len(password) > 20:
        password_error = 'password must be between 3 and 20 characters'
        password = ''
        verify = ''
    if password.count(space) != 0:
        password_error = 'password cannot contain spaces'
        password = ''
        verify = ''
    if verify != password:
        verify_error = 'Passwords do not match'
        password = ''
        verify = ''
    
    if len(email) != 0:
        if is_valid_email(email) == False:
            email_error = "Please enter a vaild email address"
            password = ''
            verify = ''

    if not username_error and not password_error and not verify_error and not email_error:
        username = request.form['username']
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup.html', username=username, username_error=username_error, 
            password=password, password_error=password_error, verify=verify, verify_error=verify_error,
            email=email, email_error=email_error)


@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome_user.html', username=username)

if  __name__ == "__main__":
    app.run()
