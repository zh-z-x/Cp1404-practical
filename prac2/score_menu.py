def main():
    score = get_valid_score()
    choice = ""
    while choice != "Q":
        print_menu()
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = get_score_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            print_stars(score)
        elif choice == "Q":
            print("Goodbye!")
        else:
            print("Invalid option")

def print_menu():
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

def get_valid_score():
    score = float(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter a valid score (0-100): "))
    return score

def get_score_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_stars(score):
    print("*" * int(score))

main()
