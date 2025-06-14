import random

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    num_picks = int(input("How many quick picks? "))
    for _ in range(num_picks):
        quick_pick = []
        while len(quick_pick) < NUMBERS_PER_LINE:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if number not in quick_pick:
                quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{num:2}" for num in quick_pick))

main()