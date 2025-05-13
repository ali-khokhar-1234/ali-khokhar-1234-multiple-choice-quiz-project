questions = ["Who is the actor that plays the character John Wick?",
             "Which country has the most lithium reserves in the world?",
             "When was insulin discovered?",
             "How many seats are in the House of Commons Canada?",
             "Where is the Merdeka 118 building located? "]

options = [("A. Matt Damon ", "B. Jason Statham ", "C. Keanu Reeves ", "D. Sylvester Stallone "),
           ("A. Argentina ", "B. Chile", "C. Australia", "D. Zimbabwe"),
           ("A. 1921", "B. 1874", "C. 1932", "D. 1899"),
           ("A. 334", "B. 313", "C. 322", "D. 343"),
           ("A. Jakarta ", "B. Nanjing", "C. Kuala Lumpur", "D. Hong Kong")]

answers = ("C", "B", "A", "D", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = str(input("Enter (A, B, C, D): ").upper())
    guesses.append(guess)
    if guess == answers[question_num]:
        print("CORRECT!")
        score += 1
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("---------------------------")
print("         RESULTS           ")
print("---------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int((score/len(questions))*100)

print(f"Your score is: {score}%")
