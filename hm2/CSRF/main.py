from flask import Flask, render_template, request, redirect
import time

app = Flask(__name__)

class Account:
    def __init__(self, name, email):
        self.name = name
        self.email = email

emails = {"victim123":"victim123@email.com"}
sessions = {}

@app.route('/')
def view_handler():
    cookie = request.cookies.get('session')
    if not cookie:
        return 'Not login yet!', 500
    account = sessions.get(cookie)
    if not account:
        return 'Invalid session', 500
    return render_template('view.html', email=account.email)

@app.route('/update', methods=['GET'])
def update_handler():
    cookie = request.cookies.get('session')
    if not cookie:
        return 'Session cookie not found', 500
    email = request.args.get('email')
    if not email:
        return 'Email missing', 500
    if cookie not in sessions:
        return 'Account not found', 500
    sessions[cookie].email = email

    return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login_handler():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Simulating a simple username and password check
        if username == 'victim123' and password == 'sec321':
            return set_session_cookie(username)
        else:
            return 'Invalid credentials', 401

def set_session_cookie(username):
    cookie = '1dd6fd9ceab04196a5b776d605078877'
    sessions[cookie] = Account(username, emails[username])
    response = redirect('/')
    response.set_cookie('session', cookie, expires=time.time() + 36000)
    return response

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=8080)
