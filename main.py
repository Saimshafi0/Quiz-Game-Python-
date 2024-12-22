print("Welcome to my computer quiz!")
playing = input("Do you want to play? ").lower()

if playing != "yes":
    print("Okay, maybe next time!")
    quit()

print("Okay! Let's play :)")
score = 0

# Question 1
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'central processing unit'.")

# Question 2
answer = input("What is the keyword used to define a function in Python? ").lower()
if answer == "def":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'def'.")

# Question 3
answer = input("Which data type is used to store True or False in Python? ").lower()
if answer == "boolean" or answer == "bool":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'boolean' or 'bool'.")

# Question 4
answer = input("What is the name of the method used to add an element to a list in Python? ").lower()
if answer == "append":
    print("Correct!")
    score += 1

else:
    print("Incorrect. The correct answer is 'append'.")

# Question 5
answer = input("What is the output of '3 ** 2' in Python? ")
if answer == "9":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is '9'.")

# Question 6
answer = input("What is the file extension for Python files? ").lower()
if answer == ".py":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is '.py'.")

print("Your final score is: ", score)
print("You got " + str((score / 6) * 100) + "%")