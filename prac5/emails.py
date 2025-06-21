"""
Emails
Estimate: 25 minutes
Actual:  22 minutes
"""
def extract_name_from_email(email):
    # Get the part before '@' in the email
    username = email.split('@')[0]
    # Split the username by '.' to separate name parts
    parts = username.split('.')
    # Capitalize the first letter of each part and join them with spaces
    name = ' '.join(part.title() for part in parts)
    return name

def main():
    email_to_name = {}  # Dictionary to store emails as keys and names as values

# Prompt the user for the first email
email = input("Email: ").strip()
# Loop as long as the email is not blank
while email != "":
    # Extract a default name from the email
    default_name = extract_name_from_email(email)
    # Ask user to confirm the extracted name
    confirm = input(f"Is your name {default_name}? (Y/n) ").strip().lower()

    # If user presses Enter or types 'y', accept the default name
    if confirm == "" or confirm == "y":
        name = default_name
    else:
        # Otherwise, ask user to enter their name manually
        name = input("Name: ").strip()

    # Store the email and confirmed name in the dictionary
    email_to_name[email] = name
    # Prompt for next email
    email = input("Email: ").strip()

    # After input ends, print all stored emails and names
for email, name in email_to_name.items():
    print(f"{name} ({email})")

if __name__ == "__main__":
    main()