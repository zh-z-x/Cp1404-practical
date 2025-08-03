from silver_service_taxi import SilverServiceTaxi

def main():
    sst = SilverServiceTaxi("Hummer", 200, 2)
    sst.start_fare()
    sst.drive(18)
    print(sst)
    fare = sst.get_fare()
    print(f"Fare for 18 km trip: ${fare:.2f}")

    expected_fare = 18 * 1.23 * 2 + 4.50
    assert abs(fare - expected_fare) < 0.01, "Fare calculation error!"

if __name__ == '__main__':
    main()
