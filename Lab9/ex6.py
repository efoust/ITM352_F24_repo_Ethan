# read a file of questions and answers and save it as a dictioanry
import json
#open the json file and load its content(dictionary)
with open("quiz.json", "r") as dictionaryfile:
    data = json.load(dictionaryfile)

    #data variable now holds the dictonary of questions. 
    print("the question dictonary is: ")
    print(data)