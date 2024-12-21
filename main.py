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

# Question 7
answer = input("What is the result of 'len([1, 2, 3, 4])'? ")
if answer == "4":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is '4'.")

# Question 8
answer = input("What does the 'break' statement do in a loop? ").lower()
if "exit" in answer or "terminate" in answer:
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'It exits or terminates the loop.'")

# Question 9
answer = input("Which method is used to remove an item by index in a Python list? ").lower()
if answer == "pop":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'pop'.")

# Question 10
answer = input("What is the result of '5 // 2' in Python? ")
if answer == "2":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is '2'.")

# Question 11
answer = input("What is the default value of the 'end' parameter in the print() function? ").lower()
if answer == "newline" or answer == "\\n":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'newline' or '\\n'.")

# Question 12
answer = input("What does the 'is' operator check for in Python? ").lower()
if "identity" in answer:
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'It checks for object identity.'")

# Question 13
answer = input("Which built-in Python function is used to convert a string to an integer? ").lower()
if answer == "int":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'int'.")

# Question 14
answer = input("What is the output of 'type(3.14)' in Python? ").lower()
if answer == "<class 'float'>" or answer == "float":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is '<class 'float'>'.")

# Question 15
answer = input("Which Python keyword is used to handle exceptions? ").lower()
if answer == "try" or answer == "except":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'try' or 'except'.")

# Question 16
answer = input("What does the 'continue' statement do in a loop? ").lower()
if "skip" in answer or "next" in answer:
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'It skips the current iteration and moves to the next.'")

print("Your final score is:", score)
print("You got " + str((score / 16) * 100) + "%")
