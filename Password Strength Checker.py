def password_strength(pwd):
    if len(pwd) < 8:
        return "Weak Password"
    if any(c.isupper() for c in pwd) and any(c.islower() for c in pwd) \
       and any(c.isdigit() for c in pwd):
        return "Strong Password"
    return "Medium Password"

password = input("Enter password: ")
print(password_strength(password))
