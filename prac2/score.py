import random

def get_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    score = float(input("Enter score: "))
    result = get_score_result(score)
    print(f"Result: {result}")

    random_score = random.randint(0, 100)
    random_result = get_score_result(random_score)
    print(f"Random score: {random_score} - {random_result}")

main()
