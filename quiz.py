# Function to run the quiz
def run_quiz(questions):
    score = 0 
    for question, data in questions.items():  # Correct indentation here
        print(f"\n{question}")
        for i, option in enumerate(data['options']):
            print(f"{i+1}. {option}")


        answer = input("Enter the number of your answer. ")

        if answer.isdigit() and int (answer) == data['answer']:
            print ("Correcto!")
            score += 1

        else: 
            print(f"Wrong! The correct answer is {data['answer']}. {data['options'][data['answer']-1]}")

    print (f"\nQuiz finished! Your final score is {score}/{len(questions)}")


# Quiz questions stored in a dictiondary
quiz_questions = {
    "What is the capital of France?": {
        "options": ["Berlin", "London", "Paris", "Madrid"],  # Use a list and commas
        "answer": 3  # The answer is an integer representing the correct option (Paris)
    },
    "Who wrote 'Hamlet'?": {
        "options": ["Leo Tolstoy", "Mark Twain", "William Shakespeare", "Charles Dickens"],
        "answer": 3
    },
    "What is the largest planet in our solar system?": {
        "options": ["Earth", "Jupiter", "Mars", "Saturn"],
        "answer": 2
    },
    "Which language is primarily spoken in Brazil?": {
        "options": ["Spanish", "Portuguese", "French", "English"],
        "answer": 2
    }
}
# Running the quiz
run_quiz(quiz_questions)