print("Welcome to Abba's computer quiz")

playing = input("Do you want to play? ")

if playing.lower() !=  "yes":
    quit()
else:
    print("okay lets play")
score = 0

answer = input("What does C.P.U stands for? ")
if answer.lower()== "Central Processing Unit":
    print("Correct!!")
    score += 1

else:
    print("Incorect")

answer = input("What does RAM stands for? ")
if answer.lower() == "Random Access Memory":
    print("Correct!!")
    score += 1
else:
    print("Incorect")

print ("You got " + str(score) + ' Questions Correct')