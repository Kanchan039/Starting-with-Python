import json
import random

quiz_data = {
    "questions": [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 5 + 7?", "answer": "12"},
        {"question": "Which planet is known as the Red Planet?", "answer": "Mars"}
    ]
}

score = 0
random.shuffle(quiz_data["questions"])

for q in quiz_data["questions"]:
    ans = input(q["question"] + " ")
    if ans.lower() == q["answer"].lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct answer: {q['answer']}\n")

print(f"Your Score: {score}/{len(quiz_data['questions'])}")
