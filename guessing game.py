
questions = (("How many elements in the priodic table? :"),
             ("How many bones are there in human body? :"),
             ("Which animal has the biggest eggs? :"),
             ("Which gas is most abundant in atmosphere? :"),
             )
options = (("A. 118","B. 117","C. 116","D. 115"),
           ("A. 205","B. 206","C. 207","D. 209"),
           ("A. Crocodile","B. Elephant","C. Whale","D. Ostrich"),
           ("A. Carbon-dioxide","B. Oxygen","C. Nitrogen","D. Hydrogen"))

answers = ("A","B","D","C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter the your answer : A, B, C, D. : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct answer ")
    else :
        print("Incorrect answer ")
        print(f"Correct answer is : {answers[question_num]}")
    question_num += 1

print("--------------------")
print("      Results       ")
print("--------------------")
print("Correct answers :-")
for answer in answers:
    print(answer, end =" ")
print()
print("Your answers are :-")
for guess in guesses:
    print(guess, end =" ")

print()
score = ( score / len(questions) ) * 100

print(f"Your score is {score} :")