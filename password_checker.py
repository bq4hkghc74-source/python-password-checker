import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = []
    if length_error:
        errors.append("Password must be at least 8 characters long.")
    if uppercase_error:
        errors.append("Password must contain at least one uppercase letter.")
    if lowercase_error:
        errors.append("Password must contain at least one lowercase letter.")
    if digit_error:
        errors.append("Password must contain at least one number.")
    if special_char_error:
        errors.append("Password must contain at least one special character.")

    if not errors:
        return "Password is strong."
    else:
        return "Password is weak:\n" + "\n".join(errors)

if __name__ == "__main__":
    password = input("Enter your password to check: ")
    result = check_password_strength(password)
    print(result)
