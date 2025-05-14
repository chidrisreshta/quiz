import time

# Sample questions organized by category
questions = {
    "General Knowledge": [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Paris", "C. Rome", "D. Madrid"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Saturn", "C. Mars", "D. Jupiter"],
            "answer": "C"
        }
    ],
    "Science": [
        {
            "question": "What gas do plants absorb from the atmosphere?",
            "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
            "answer": "C"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A. CO2", "B. H2O", "C. O2", "D. H2"],
            "answer": "B"
        }
    ]
}

# Track score and answers
score = 0
total_questions = 0
review = []

print("Welcome to the Quiz Game!\n")
print("Choose a category:")
categories = list(questions.keys())

for idx, cat in enumerate(categories):
    print(f"{idx + 1}. {cat}")

try:
    choice = int(input("Enter the number of your chosen category: "))
    category = categories[choice - 1]
except (ValueError, IndexError):
    print("Invalid choice. Defaulting to 'General Knowledge'.")
    category = "General Knowledge"

print(f"\nYou selected: {category}")
print("You will have 10 seconds to answer each question.\n")
time.sleep(1)

for q in questions[category]:
    total_questions += 1
    print("\n" + q["question"])
    for opt in q["options"]:
        print(opt)
    
    start_time = time.time()
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    end_time = time.time()

    if end_time - start_time > 10:
        print("⏰ Time's up! No points awarded.")
        review.append((q["question"], "Timed out", q["answer"]))
        continue

    if answer == q["answer"]:
        print("✅ Correct!")
        score += 1
        review.append((q["question"], answer, "Correct"))
    else:
        print(f"❌ Wrong! The correct answer was {q['answer']}.")
        review.append((q["question"], answer, q["answer"]))

# Final Score
print("\nQuiz Completed!")
print(f"Your Score: {score} / {total_questions}")

# Answer Review
print("\nAnswer Review:")
for q, user_ans, correct_ans in review:
    print(f"- {q}")
    print(f"  Your answer: {user_ans}")
    if user_ans != "Correct":
        print(f"  Correct answer: {correct_ans}")
    print()

