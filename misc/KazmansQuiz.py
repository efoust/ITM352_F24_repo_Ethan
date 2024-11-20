# Quiz app using Flask 
from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global question_num, score

    if request.method == 'POST':
        # Logic to capture the user’s answers and redirect to the result page
        score += 1
        return redirect(url_for('result',score=score))
    
    # Load the question and options to display
    question_num += 1
    return render_template('quiz.html', num=question_num,
                           question=question_list[question_num-1][0], 
                            options=question_list[question_num-1][1])  # Displays the question and options


@app.route('/result')
def result():
    global score
    
    return render_template('result.html', score=score)

# Load the question file and convert it to a list
question_file = open("questions.json")
questions = json.load(question_file)
question_list = list(questions.items())

# Create some housekeeping variables
score = 0
question_num = 0

# Run the application
if __name__ == "__main__":
    app.run(debug=True)