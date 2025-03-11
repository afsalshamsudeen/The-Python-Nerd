
print('Welcome to the Computer Quiz!')
playingornot = input("Do you want to play this game? yes/no ")


if playingornot.lower() != "yes":
    quit()
print('Fantastic lets continue!')
score = 0

QnA = input("What does CPU stand for? ")

if QnA.lower() == "central processing unit":
    print('Correct Answer :)')
    score += 1
else:
    print("Incorrect Answer :(")

QnA = input("Which programming language is primarily used for web development alongside HTML and CSS? ")

if QnA.lower() == "javascript":
    print('Correct Answer :)')
    score += 1
else:
    print("Incorrect Answer :(")

QnA = input("What is the name of the first computer virus? ")

if QnA.lower() == "creeper":
    print('Correct Answer :)')
    score += 1
else:
    print("Incorrect Answer :(")

QnA = input("Which data structure uses the LIFO (Last In, First Out) principle? ")

if QnA.lower() == "stack":
    print('Correct Answer :)')
    score += 1
else:
    print("Incorrect Answer :(")

QnA = input("What does RAM stand for? ")

if QnA.lower() == "random access memory":
    print('Correct Answer :)')
    score += 1
else:
    print("Incorrect Answer :(")

QnA = input("Which company developed the Windows operating system? ")

if QnA.lower() == "microsoft":
    print('Correct Answer :)')
    score += 1
else:
    print("Incorrect Answer :(")

print("Congratulations You Finished The Game Successfully!")
print("Your Score= "+str(score))
print("Your Score= "+str((score/6)*100)+"%")