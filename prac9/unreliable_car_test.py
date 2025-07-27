from unreliable_car import UnreliableCar

def main():
    """Test UnreliableCar with multiple drive attempts."""

    reliable_car = UnreliableCar("ReliableCar", 100, 90.0)
    unreliable_car = UnreliableCar("UnreliableCar", 100, 10.0)

    print("Testing ReliableCar:")
    reliable_drives = 0
    for _ in range(100):
        if reliable_car.drive(1) > 0:
            reliable_drives += 1
    print(f"ReliableCar successful drives: {reliable_drives}/100")

    print("\nTesting UnreliableCar:")
    unreliable_drives = 0
    for _ in range(100):
        if unreliable_car.drive(1) > 0:
            unreliable_drives += 1
    print(f"UnreliableCar successful drives: {unreliable_drives}/100")

if __name__ == '__main__':
    main()