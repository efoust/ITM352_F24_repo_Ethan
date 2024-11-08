#qiz app using flask
#Create a simple log in page 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

#asking a question
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Logic to capture the user’s answers and redirect to the result page
        return redirect(url_for('result'))
    # Load the question and options to display
    return render_template('quiz.html')  # Displays the question and options


@app.route('/result')
def result():
    # Calculate and display the user's score
    score = 1  # Example score for demonstration
    return render_template('result.html', score=score)



USERS = {
    "port": "port123",
    "kazman": "kazman123"
}

if __name__ == "__main__":
    app.run(debug=True)