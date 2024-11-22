# Quiz app using Flask 
from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
from datetime import datetime

app = Flask(__name__)

app.secret_key = 'ethan'

def load_users():
    with open('user.json') as user_file:
        users = json.load(user_file)
    return users["users"]

@app.route("/")
def home():
    global question_num, score, start_time
    question_num = 0
    score = 0
    start_time = datetime.now()
    return render_template('home.html')


@app.route('/login', methods = ['GET','POST'])
def login():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()

        for user in users:
            if user['username'] == username and user['password'] == password:
                session['username'] = username
                return redirect(url_for('home'))
        #flash('Invalid credentials, please try again')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'username' not in session:
        return redirect(url_for('login'))

    global question_num, score, hint
    result = None
    hint = None

    correct_message = 'Nice! Your answer was Correct!'
    incorrect_message = 'Sorry! Your answer was Incorrect!'

    if request.method == 'POST':
        if request.form.get("action") == 'hint':
            hint= question_list[question_num].get("hint","No hint available")
        else:
            # Logic to capture the user’s answers and redirect to the result page
            user_answer = request.form.get("answer")
            correct_answer = question_list[question_num]["answer"]
            if user_answer == correct_answer:
                score += 1
                result = correct_message
            else: 
                result = incorrect_message
            
            question_num += 1
            if question_num >= len(question_list):
                #save_score(session['username'], score, len(question_list))
                return redirect(url_for('result',score=score))
            
    
    #Load the question and options to display
    return render_template('quiz.html', num=question_num + 1,
                           question=question_list[question_num]["question"], 
                            options=question_list[question_num]["options"],
                             result = result, hint = hint)  # Displays the question and options



@app.route('/result')
def result():
    global score_percentage, time_taken, displayed_time

    if 'username' not in session:
        return redirect(url_for('login'))
    
    end_time = datetime.now() 
    time_taken = end_time - start_time

    get_seconds = time_taken.total_seconds()
    get_minutes = get_seconds/60
    get_hours = get_minutes/60

    formatted_minutes = int(get_minutes)
    formatted_seconds = int(get_seconds)
    formatted_hours = int(get_hours)

    if(formatted_hours >= 1):
        displayed_time = f"You took {formatted_hours} hours and {formatted_minutes} minutes and {formatted_seconds} seconds to complete this quiz."
    elif(formatted_minutes >= 1):
        displayed_time = f"You took {formatted_minutes} minutes and {formatted_seconds} seconds to complete this quiz."
    else:
        displayed_time = f"You took {formatted_seconds} seconds to complete this quiz."

    

    score_percentage = score/question_num * 100
    score_percentage = int(score_percentage)

    return render_template('result.html', score=score, question_num = question_num, score_percentage = score_percentage, displayed_time = displayed_time, time_taken = time_taken)

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

