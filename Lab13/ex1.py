#first flask application example
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return("Hello World! <p>My site is still empty</p>")

#Run the application
if __name__ == "__main__":
    app.run(debug=True)

