# Quiz app using Flask 
from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route("/")
def home():
    global question_num, score
    question_num = 0
    score = 0
    return render_template('home.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global question_num, score

    if request.method == 'POST':
        # Logic to capture the user’s answers and redirect to the result page
        user_answer = request.form.get("answer")
        correct_answer = question_list[question_num]["answer"]
        if user_answer == correct_answer:
            score += 1
        question_num += 1
        if question_num >= len(question_list):
            return redirect(url_for('result',score=score))
    
    #Load the question and options to display
    return render_template('quiz.html', num=question_num + 1,
                           question=question_list[question_num]["question"], 
                            options=question_list[question_num]["options"])  # Displays the question and options


@app.route('/result')
def result():
    
    return render_template('result.html', score=score, question_num = question_num)

# Load the question file and convert it to a list
#question_file = open("questions.json")
#questions = json.load(question_file)
#question_list = list(questions.items())
with open("questions.json") as question_file:
    question_list = json.load(question_file)["questions"]

# Create some housekeeping variables
score = 0
question_num = 0

# Run the application
if __name__ == "__main__":
    app.run(debug=True)