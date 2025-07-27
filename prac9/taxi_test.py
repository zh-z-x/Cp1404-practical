from taxi import Taxi

def main():
    """Test the Taxi class with a sample scenario."""

    # 1. Create a new Taxi object
    my_taxi = Taxi("Prius 1", 100)

    # 2. Drive the taxi 40 km
    my_taxi.drive(40)

    # 3. Print the taxi details and current fare
    print(my_taxi)
    print("Current fare: ${:.2f}".format(my_taxi.get_fare()))

    # 4. Restart the fare meter
    my_taxi.start_fare()

    # 5. Drive the taxi 100 km
    my_taxi.drive(100)

    # 6. Print the taxi details and current fare
    print(my_taxi)
    print("Current fare: ${:.2f}".format(my_taxi.get_fare()))

if __name__ == '__main__':
    main()
