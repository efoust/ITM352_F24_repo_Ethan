#qiz app using flask
#Create a simple log in page 
from flask import Flask, render_template, request, redirect, url_for
import json
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

#asking a question
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global question_num, score
    if request.method == 'POST':
        # Logic to capture the user’s answers and redirect to the result page
        #if ____
        score += 1
        return redirect(url_for('result',score=score))
    # Load the question and options to display
    question_num += 1
    return render_template('quiz.html',
                           num=question_num, 
                           question=question_list[question_num-1][0],options=question_list[question_num-1][1] )  # Displays the question and options


@app.route('/result')
def result():
    # Calculate and display the user's score
    return render_template('result.html', score=score)

#Load the question file and convert it to a list
question_file = open("questions.json")
questions = json.load(question_file)
question_list = list(questions.items())

#housekeeping variables
score = 0
question_num = 0

USERS = {
    "port": "port123",
    "kazman": "kazman123"
}

if __name__ == "__main__":
    app.run(debug=True)