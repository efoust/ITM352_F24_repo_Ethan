from flask import Flask, render_template, request, redirect, url_for, session, flash
import json

app = Flask(__name__)
app.secret_key = 'ethan'

# Load user file to validate the login page
def load_users():
    try:
        with open('user.json') as user_file:
            users = json.load(user_file)
        return users["users"]
    except FileNotFoundError:
        return []


# Home page
@app.route("/")
def home():
    session['question_num'] = 0
    session['user_responses'] = {}
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        users = load_users()
        for user in users:
            if user['username'] == username:
                flash("Username already exists. Please choose another one.")
                return redirect(url_for('register'))
        
        new_user = {'username': username, 'password': password}
        users.append(new_user)
        
        with open('user.json', 'w') as user_file:
            json.dump({'users': users}, user_file, indent=4)
        
        flash("Registration successful! Please log in.")
        return redirect(url_for('login'))
    
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        for user in users:
            if user['username'] == username and user['password'] == password:
                session['username'] = username
                return redirect(url_for('home'))
        flash("Invalid username or password")
    return render_template('login.html')

#logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

# Quiz route
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    question_num = session.get('question_num', 0)
    user_responses = session.get('user_responses', {})
    
    if request.method == 'POST':
        if request.form.get('next'):
            question_num += 1
            if question_num >= len(question_list):
                session['question_num'] = question_num
                return redirect(url_for('result'))
        else:
            # Capture user response
            user_answer = request.form.get("answer", "").strip()
            if user_answer:
                question_key = question_list[question_num]["question"]
                user_responses[question_key] = user_answer
                print(f"User response added: {question_key} - {user_answer}")
            question_num += 1
            if question_num >= len(question_list):
                session['user_responses'] = user_responses
                session['question_num'] = question_num
                return redirect(url_for('result'))

        session['question_num'] = question_num
        session['user_responses'] = user_responses

    progress = (question_num + 1) / len(question_list) * 100
    return render_template('quiz.html', num=question_num + 1,
                           question=question_list[question_num]["question"],
                           options=question_list[question_num]["options"],
                           progress=progress)

def recommend_movies(user_responses, movies):
    user_genre = user_responses.get('What genre of movie do you like?').lower()
    user_platform = user_responses.get('Which platform do you prefer to watch movies on?').lower()
    user_rating = user_responses.get('Do you have a preferred movie rating?').upper()
    recommended_movies = []

    for genre, movie_list in movies["movies"]["genres"].items():
        if user_genre == genre.lower():
            print(f"Genre match found: {genre}")  # Debugging
            for movie in movie_list:
                print(f"Evaluating movie: {movie['title']}")  # Debugging
                if user_platform and user_platform not in [p.lower() for p in movie["platform"]]:
                    print(f"Skipping movie {movie['title']} because platform {movie['platform']} does not match user preference {user_platform}")  # Debugging
                    continue
                if user_rating and movie["rating"].upper() != user_rating:
                    print(f"Skipping movie {movie['title']} because rating {movie['rating']} does not match user preference {user_rating}")  # Debugging
                    continue
                print(f"Adding movie {movie['title']} to recommendations")  # Debugging
                recommended_movies.append(movie['title'])

    print("Recommended Movies:", recommended_movies)  # Debugging
    return recommended_movies


@app.route('/watchlist') 
def watchlist(): 
    if 'username' not in session: 
        return redirect(url_for('login')) 
    
    username = session['username'] 
    with open('watchlist.json') as file: 
        watchlist_data = json.load(file) 
        
        user_watchlist = watchlist_data['watchlists'].get(username, []) 
        return render_template('watchlist.html', watchlist=user_watchlist)

@app.route('/add_to_watchlist', methods=['POST'])
def add_to_watchlist():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    movie_title = request.form.get('movie_title')
    
    with open('watchlist.json', 'r+') as file:
        watchlist_data = json.load(file)
        if username not in watchlist_data['watchlists']:
            watchlist_data['watchlists'][username] = []
        if movie_title not in watchlist_data['watchlists'][username]:
            watchlist_data['watchlists'][username].append(movie_title)
            file.seek(0)
            json.dump(watchlist_data, file, indent=4)
            file.truncate()
    
    flash(f"{movie_title} has been added to your watchlist!")
    return redirect(url_for('result'))

@app.route('/remove_from_watchlist', methods=['POST'])
def remove_from_watchlist():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    movie_title = request.form.get('movie_title')
    
    with open('watchlist.json', 'r+') as file:
        watchlist_data = json.load(file)
        if 'watchlists' in watchlist_data and username in watchlist_data['watchlists']:
            if movie_title in watchlist_data['watchlists'][username]:
                watchlist_data['watchlists'][username].remove(movie_title)
                file.seek(0)
                json.dump(watchlist_data, file, indent=4)
                file.truncate()
    
    flash(f"{movie_title} has been removed from your watchlist.")
    return redirect(url_for('watchlist'))

@app.route('/result')
def result():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    with open('movies.json') as movies_file:
        movies = json.load(movies_file)
    
    user_responses = session.get('user_responses', {})
    print("Final User Responses:", user_responses)  # Debugging
    recommendations = recommend_movies(user_responses, movies)
    print("Recommendations passed to template:", recommendations)  # Debugging

    return render_template('result.html', recommendations=recommendations)

# Convert questions.json into a list of questions
with open("questions.json") as question_file:
    question_list = json.load(question_file)["questions"]

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
