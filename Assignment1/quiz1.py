#Quiz application that asks the user 3 multiple choice questions. 
#presents all the possible answers to the question(multiple choice)
#accept an answer from the user a,b,c, or d and determine right or wrong
#print write or wrong. 
#only accept characters a b c and d(ignore and re-ask question)
#store quiz questions in a file
import json

def load_questions(dictFile):
    with open(dictFile, "r") as file:
        questions = json.load(file)
    return questions


letters = ['a', 'b', 'c', 'd']
#with open("quizQs.json", "r") as questions:
#    data = json.load(questions)
def quiz (question, alternatives):
        #defines the correct answers
        correctAnswer = alternatives[0]
        #prints the question 
        print(f"\n{question}? \nYour answer should submitted as a, b, c, or d. ")
        #print multiple choice answers
        for i, alternative in enumerate(alternatives):
            print(f"{letters[i]}. {alternative}")
            #asks if user would like a hint
        hint = input("Would you like a hint? Respond with yes or no. ")
            #if the user types yes, a hint is given.
        if(hint == "yes"):
            print("Hint: the answer is A")
        #ask for the user to input their answer and validates it is one of the options provided. 
        while True:
            answer = input(f"What is the correct answer? ")
            #makes sure the value entered is one of the possible answers
            if answer in letters: 
            #takes answer and finds the corrosponding value in the dictonary saves as a variable
                selected_answer = alternatives[letters.index(answer)]
                break
            else:
                print("The answer you submitted was not one of the given options, please respond with a, b, c, or d. ")

            #checks if the answer is correct prints right or wrong, returns true or false for the counter. 
        if selected_answer == correctAnswer:
            print(f"You are correct!\n{selected_answer} is the correct answer!")
            return True
        else: 
            print(f"Incorrect! The correct answer is {correctAnswer}")
            return False

#loads the quiz questions and defines them in a variable
dictQuestions = load_questions("quizQs.json")    
#initialize counter
correctCount = 0
totalQuestions = len(dictQuestions)
#load the questions from the json file

#calls the function defined aboove. (Starts the program)
for question, alternatives in dictQuestions.items():
    #adds 1 to the counter when the answer is correct
    if quiz(question, alternatives):
        correctCount +=1
#calculate the users score on the quiz
score = (correctCount/totalQuestions)*100
#prints the score
print(f"\rYou scored {round(score,2)}%")
#defines test results to copy to the new file. 
testResults = {
    #how many questions were answered correctly
    "Questions Correct": correctCount,
    #how many total questions in the quiz
    "Total Questions": totalQuestions,
    #test score as a percentage. 
    "Score as a percentage": score
}
#a variable containing the name of the file storing test scores.
testScores = "scores.json"
#creates and dumps the test result dictionary into the new json file. 
with open(testScores, "w") as json_file:
    json.dump(testResults, json_file, indent=4)