# Quiz app 
from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
from datetime import datetime

app = Flask(__name__)

app.secret_key = 'ethan'
#load user file in order to validate the login page
def load_users():
    with open('user.json') as user_file:
        users = json.load(user_file)
    return users["users"]

#home page
@app.route("/")
def home():
    global question_num, score, start_time
    question_num = 0
    score = 0
    start_time = datetime.now()
    return render_template('home.html')

#login route displays provides content for login page, checks if username matches an established username in the user.json file
#saves what the user has submitted into a variable. if the login info is correct, move to the home pagee.
@app.route('/login', methods = ['GET','POST'])
def login():
    global username, password
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        print(username,password)
        for user in users:
            if user['username'] ==  username and user['password'] == password:
                session['username'] = username
                return redirect(url_for('home'))
    return render_template('login.html')



#logout back to home page, clear username from session
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))
#Quiz route
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
       #make global and reset variables
        global question_num, score, hint
        result = None
        hint = None
        #define variables for result 
        correct_message = 'Nice! Your answer was Correct!'
        incorrect_message = 'Sorry! Your answer was Incorrect!'
        
        if request.method == 'POST':
            #check if hint button is pressed
            if request.form.get("action") == 'hint':
                hint= question_list[question_num].get("hint","No hint available")
            elif request.form.get('next'):
                question_num += 1
                if question_num >= len(question_list):
                    return redirect(url_for('result',score=score))
            else:
                user_answer = request.form.get("answer")
                correct_answer = question_list[question_num]["answer"]
                if user_answer == correct_answer:
                    score += 1
                    result = correct_message
                else: 
                    result = incorrect_message            
        progress = (question_num + 1) / len(question_list) * 100    
    #Load the question and options to display
    return render_template('quiz.html', num=question_num + 1,
                           question=question_list[question_num]["question"], 
                            options=question_list[question_num]["options"],
                             result = result, hint = hint, progress = progress)  # Displays the question and options



@app.route('/result')
def result():
    global score_percentage, time_taken, displayed_time, scores_data
    #check if user logged in
    if 'username' not in session:
        return redirect(url_for('login'))
    
   
    #calculate results for the results page and to save to scores.json

    end_time = datetime.now() 
    time_taken = end_time - start_time

    get_seconds = time_taken.total_seconds()
    get_minutes = get_seconds/60
    get_hours = get_minutes/60

    formatted_minutes = int(get_minutes)
    formatted_seconds = int(get_seconds)
    formatted_hours = int(get_hours)

    score_percentage = score/question_num * 100
    score_percentage = int(score_percentage)

    #display how long the quiz took with words
    if(formatted_hours >= 1):
        displayed_time = f"You took {formatted_hours} hours and {formatted_minutes} minutes and {formatted_seconds} seconds to complete this quiz."
    elif(formatted_minutes >= 1):
        displayed_time = f"You took {formatted_minutes} minutes and {formatted_seconds} seconds to complete this quiz."
    else:
        displayed_time = f"You took {formatted_seconds} seconds to complete this quiz."

    #format display for scores.json and save into a variable
    scores_data = {
                        "username": session['username'],
                        "score": score,
                        "score percentage": score_percentage,
                        "time_taken": [formatted_hours, formatted_minutes, formatted_seconds],
                        "total_questions": len(question_list)
                        
    }
    #load scores.json and pass the data from scores_data into the file. saving scores
    try:
        with open('scores.json', 'r+') as scores_file:
            try:
                data = json.load(scores_file)
            except json.JSONDecodeError:
                data = {"scores": []}
            data["scores"].append(scores_data)
            scores_file.seek(0) 
            json.dump(data, scores_file, indent=4)
    except FileNotFoundError : 
        with open('scores.json', 'w') as scores_file:
            json.dump({"scores": [scores_data]}, scores_file, indent=4)

    return render_template('result.html', score=score, question_num = question_num, score_percentage = score_percentage, displayed_time = displayed_time, time_taken = time_taken)

#convert questions.json into a list of questions
with open("questions.json") as question_file:
    question_list = json.load(question_file)["questions"]

# Create some housekeeping variables
score = 0
question_num = 0

# Run the application
if __name__ == "__main__":
    app.run(debug=True)

