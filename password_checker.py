import re

def check_password_strength(password):
    # Define the criteria for a strong password
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    number_criteria = re.search(r'[0-9]', password)
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    # Check if all criteria are met
    if all([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria]):
        return "Strong"
    elif length_criteria and (uppercase_criteria or lowercase_criteria) and (number_criteria or special_char_criteria):
        return "Moderate"
    else:
        return "Weak"

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength = check_password_strength(password)
    print(f"The password strength is: {strength}")
