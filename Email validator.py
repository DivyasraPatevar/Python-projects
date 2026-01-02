def is_valid_email(email):
    return "@" in email and "." in email

email = input("Enter email: ")
print("Valid Email" if is_valid_email(email) else "Invalid Email")
