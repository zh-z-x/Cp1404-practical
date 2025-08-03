from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def choose_taxi(taxis):
    display_taxis(taxis)
    choice = input("Choose taxi: ")
    if choice.isdigit():
        choice = int(choice)
        if 0 <= choice < len(taxis):
            return taxis[choice]
    print("Invalid taxi choice")
    return None

def get_positive_float(prompt):
    value = input(prompt)
    if value.replace('.', '', 1).isdigit():
        number = float(value)
        if number >= 0:
            return number
    print("Invalid input; please enter a positive number")
    return None

def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    total_bill = 0.0
    running = True

    print("Let's drive!")

    while running:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == 'q':
            running = False
        elif choice == 'c':
            taxi = choose_taxi(taxis)
            if taxi:
                current_taxi = taxi
            print(f"Bill to date: ${total_bill:.2f}")
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = get_positive_float("Drive how far? ")
                if distance is not None:
                    current_taxi.start_fare()
                    distance_driven = current_taxi.drive(distance)
                    trip_cost = current_taxi.get_fare()
                    total_bill += trip_cost
                    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
            print(f"Bill to date: ${total_bill:.2f}")
        else:
            print("Invalid option")
            print(f"Bill to date: ${total_bill:.2f}")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

if __name__ == '__main__':
    main()
