"""
CP1404/CP5632 Practical
State names in a dictionary
"""

# Reformatted dictionary to follow PEP 8 style
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}
# Print all state codes and names using aligned formatting
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")

# Convert user input to uppercase to allow lowercase entries
state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    else:
        print("Invalid short state")
    # Convert input again for the next loop iteration
    state_code = input("Enter short state: ").upper()