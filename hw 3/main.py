from flask import Flask , request, send_from_directory, render_template, redirect, make_response
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__, template_folder='template')

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user": "123"
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return users.get(username) == password
    return False

@app.route('/')
@auth.login_required
def index():
   return render_template('index.html')
    
@app.route('/cabinet/')
@auth.login_required
def cabinet():
    return render_template('cabinet.html')


@app.route('/31.jpg')
def im1():
    return app.send_static_file('31.jpg')
    
@app.route('/33.jpg')
def im2():
    return app.send_static_file('33.jpg')

@app.route('/11.jpg')
def im3():
    return app.send_static_file('11.jpg')
      
@app.route('/static/')
def imgg(path):
    return send_from_directory('static', path)


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)