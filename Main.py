import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        'Too Short': length_error,
        'No Digit': digit_error,
        'No Uppercase': uppercase_error,
        'No Lowercase': lowercase_error,
        'No Special Character': symbol_error
    }

    score = 5 - sum(errors.values())
    
    if score == 5:
        strength = "Very Strong 💪"
    elif score >= 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak ⚠"

    return strength, [error for error, has_error in errors.items() if has_error]

# Example usage
if _name_ == "_main_":
    user_password = input("Enter a password to check its strength: ")
    strength, issues = check_password_strength(user_password)
    print(f"\nPassword Strength: {strength}")
    if issues:
        print("Issues:")
        for issue in issues:
            print(f" - {issue}")
    else:
        print("Your password is strong and secure! ✅")
