username = input("Username: ")
password = input("Password: ")
email = input("Email: ")

#username validation
if (0 < len(username) <= 50):
    print("Username is valid")
else:
    print("Username is invalid")

#password validation
is_special = False
is_upper = False
is_lower = False
special_chars = "!@#$%^&*(),.?\":{}|<>"

if len(password) >= 8:
    for char in password:
        if char in special_chars:
            is_special = True
        elif char.isupper():
            is_upper = True
        elif char.islower():
            is_lower = True
if len(password) >= 8 and is_special and is_upper and is_lower:
    print("Password is Valid")
else:
    print("Password is Invalid")

#email validation
if '@' in email:
    at_index = email.index('@')
    # Check if '@' is not the first or the last character
    if at_index > 0 and at_index < len(email) - 1:
        first_part = email[:at_index]
        second_part = email[at_index + 1:]

        # Check if the first part contains only alphanumeric characters
        first_valid = True
        for char in first_part:
            if not (char.isalnum() or char in '._-'):
                first_valid = False
                break

        # Check if the second part contains exactly one dot between letters
        second_valid = True
        dot_count = 0
        if '.' in second_part:
            dot_index = second_part.find('.')
            # Ensure there is exactly one dot and it is not at the start or end
            if dot_index > 0 and dot_index < len(second_part) - 1:
                for char in second_part:
                    if char == '.':
                        dot_count += 1
                        if dot_count > 1:
                            second_valid = False
                            break
                    elif not char.isalpha():
                        second_valid = False
                        break
            else:
                second_valid = False
        else:
            second_valid = False

        # Ensure there is exactly one dot in the second part
        if dot_count != 1:
            second_valid = False

        if first_valid and second_valid:
            print("Email is valid")
        else:
            print("Email is invalid")
    else:
        print("Email is invalid")
else:
    print("Email is invalid")

