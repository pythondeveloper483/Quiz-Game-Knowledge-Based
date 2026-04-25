import random
import time
import os

# Questions bank and you can add more question as you wanted
questions = [
    {
        "question": "What is the capital of Nepal?",
        "options": ["A. Kathmandu", "B. Pokhara", "C. Biratnagar", "D. Janakpur"],
        "answer": "A"
    },
    {
        "question": "Which language is used for web structure?",
        "options": ["A. Python", "B. HTML", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit", "B. Computer Personal Unit", "C. Control Program Utility", "D. Central Power Unit"],
        "answer": "A"
    },
    {
        "question": "What does RAM stand for?",
        "options": ["A. Read Access Memory", "B. Random Access Memory", "C. Rapid Access Memory", "D. Remote Access Memory"],
        "answer": "B"
    }
]

LEADERBOARD_FILE = "leaderboard.txt"

def run_quiz(player_name):
    score = 0
    random.shuffle(questions)  # Shuffle is used to Randomize question order
    print(f"\nWelcome {player_name}! You have 10 seconds per question.\n")

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        start_time = time.time()
        answer = input("Enter your answer (A/B/C/D): ").upper()
        elapsed = time.time() - start_time

        if elapsed > 10:
            print("⏰ Time's up! No points awarded.\n")
            continue

        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

    print(f"Your final score is {score}/{len(questions)}")
    save_score(player_name, score)
    show_leaderboard()

def load_scores():
    scores = {}
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as file:
            for line in file:
                if ": " in line:
                    name, score = line.strip().split(": ")
                    scores[name] = int(score)
    return scores

def save_score(player_name, score):
    scores = load_scores()
    # Updated only if new score is higher otherwise the same score is displaying 
    if player_name not in scores or score > scores[player_name]:
        scores[player_name] = score

    # Rewrite leaderboard file with updated scores
    with open(LEADERBOARD_FILE, "w") as file:
        for name, sc in scores.items():
            file.write(f"{name}: {sc}\n")

def show_leaderboard():
    print("\n🏆 Leaderboard 🏆")
    scores = load_scores()
    if not scores:
        print("No scores yet. Be the first to play!")
        return

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for i, (name, score) in enumerate(sorted_scores[:5], start=1):
        print(f"{i}. {name}: {score}")

if __name__ == "__main__":
    name = input("Enter your name: ")
    run_quiz(name)
