# Question 1: Write name to file using open and close
name = input("Enter your name: ")
file = open('name.txt', 'w')
file.write(name)
file.close()

# Question 2: Read name from file and print greeting using open and close
file = open('name.txt', 'r')
name = file.read()
file.close()
print(f"Hi {name}!")

# Question 3: Read first two numbers from numbers.txt and add them using with
with open('numbers.txt', 'r') as file:
    first_line = file.readline()
    second_line = file.readline()
    total = int(first_line.strip()) + int(second_line.strip())
print(total)  # Should print 59 (17 + 42)

# Question 4: Calculate total of all numbers in numbers.txt using with
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line.strip())
print(total)  # Should print 459 (17 + 42 + 400)
