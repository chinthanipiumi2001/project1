quiz = {
    "question1": {
        "question": "What is the capital city of Sri Lanka?",
        "answer": "Sri Jayawardhanapura Kotte"
    },
    "question2": {
        "question": "What is the national tree of Sri Lanka?",
        "answer": "Naa Tree"
    },
    "question3": {
        "question": "What is the national sport in Sri Lanka?",
        "answer": "Volley ball"
    },
    "question4": {
        "question": "Who is the current President of Sri Lanka?",
        "answer": "Mr.Ranil Wikramasighe"
    },"question5": {
        "question": "What is the national flower of Sri Lanka?",
        "answer": "Blue water Lily"
    },"question6": {
        "question": "What is the national gem of Sri Lanka?",
        "answer": "Blue Sapphire"
    },"question7": {
        "question": "Who is the national animal of Sri Lanka?",
        "answer": "Sand chicken"
    },
}

score = 0

for key, value in quiz.items():
    print(value[' Question'])
    answer = input("Answer? ")

    if answer.lower() == value[ 'answer'] . lower():
        print('Correct')
        score = score + 1
        print("Your score is: " + str(score))
        print("")
        print("")
    else:
        print("Wrong!")
        print("The answer is : " + value[ ' answer'])
        print("Your score is: " + str(score))
        print("")
        print("")

print("You got " + str(score) + " out of 7 questions correctly")
print("Your percentage is " + str(int(score/7 * 100)) + "%")
