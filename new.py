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

def recommend_movies(user_responses, movies):
     genre = user_responses.get('What genre of movie do you like?') 
     platform = user_responses.get('Which platform do you prefer to watch movies on?') 
     rating = user_responses.get('Do you have a preferred movie rating?') 
     actors = user_responses.get('Which actors do you like? (choose at least one)', []) 
     director = user_responses.get('Do you have a favorite director?') 
     country = user_responses.get('Do you have a preferred country of origin for movies?') 
     recommended_movies = []
    
     for genre_key, movie_list in movies["movies"].items(): 
            if genre and genre != genre_key:            
                continue
            for movie in movie_list:
                if (platform and platform not in movie['platform']):
                    continue
                if (rating and movie['rating'] != rating):
                    continue
                if (actors and not any(actor in movie['actors'] for actor in actors)):
                    continue
                if (director and movie['director'] != director):
                    continue
                if (country and movie['country'] != country):
                    continue
                recommended_movies.append(movie)
        
     return recommended_movies


@app.route('/result')
def result():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    with open('movies.json') as movies_file:
        movies = json.load(movies_file)
    
    recommendations = recommended_movies(user_responses, movies)

    return render_template('result.html', recommendations=recommendations, question_num = question_num, score_percentage = score_percentage, displayed_time = displayed_time, time_taken = time_taken)

#convert questions.json into a list of questions
with open("questions.json") as question_file:
    question_list = json.load(question_file)["questions"]

# Create some housekeeping variables

question_num = 0
user_responses = {}

# Run the application
if __name__ == "__main__":
    app.run(debug=True)

