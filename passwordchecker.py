symbols = "!@#$%^&*"

while True:
    password = input("Enter password: ")

    upper = 0
    lower = 0
    digit = 0
    symbol = 0

    if len(password) < 8:
        print("Password should have at least 8 characters")
        continue

    for ch in password:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digit += 1
        elif ch in symbols:
            symbol += 1

    if upper == 0:
        print("Please include at least one CAPITAL letter")
    elif lower == 0:
        print("Please include at least one small letter")
    elif digit == 0:
        print("Please include at least one number")
    elif symbol == 0:
        print("Please include at least one symbol like @ or #")
    else:
        print("✅ Password accepted")
        break

    print("Please try again\n")
