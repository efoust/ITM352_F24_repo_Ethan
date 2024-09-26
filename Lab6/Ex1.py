# Create a conditional expression that prints true if the last element of a tuple is
# "happy" and the tuple contains more than 3 elements.

emotions = ("sad", "fear", "jealousy", "anger", "surprise", "happy")

#print((len(emotions) > 3) and (emotions[len(emotions)-1] == "happy"))

if ((len(emotions) > 3) and (emotions[len(emotions)-1] == "happy")):
    print("True")
else:
    print("False")