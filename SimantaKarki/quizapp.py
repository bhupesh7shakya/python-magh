def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    answer = input("Please enter the number of your answer: ")
    
    if answer.isdigit() and int(answer) == correct_answer:
        print("Correct!\n")
        return True
    else:
        print("Incorrect.\n")
        return False
def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "London", "Paris", "Madrid"],
            "correct_answer": 3
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "correct_answer": 2
        },
        {
            "question": "Who wrote The Alchemist?",
            "options": ["Harper Lee", "Paulo Coleho", "Ernest Hemingway", "Anton Chekov"],
            "correct_answer": 2
        }
    ]
    score = 0
    for q in questions:
        if ask_question(q["question"], q["options"], q["correct_answer"]):
            score += 1

    print(f"Your final score is: {score}/{len(questions)}")
if __name__ == "__main__":
    run_quiz()