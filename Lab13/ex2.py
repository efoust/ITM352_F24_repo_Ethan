#Create a simple log in page 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userid = request.form.get('username')
        userpass = request.form.get('password')
#Check the username and password. if successful take the user to the success page.
        if USERS.get(userid) == userpass:
            return redirect(url_for('success', username=userid))
        else:
            return("incorrect username or password")
    else:
        return render_template('login.html')
#Run the application

@app.route('/success/<username>')
def success(username):
    return render_template('success.html', username=username)

if __name__ == "__main__":
    app.run(debug=True)

USERS = {
    "port": "port123",
    "kazman": "kazman123"
}