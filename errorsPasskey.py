"""
CSci 127 Teaching Staff
March 2026
Modified by:  ADD YOUR NAME HERE
"""

def password_strength(password):
    """Takes a password string as input.
    Returns 'Weak', 'Medium', or 'Strong' based on the password's characteristics.
    A password shorter than 8 characters is always 'Weak'.
    """

    if len(password) < 8:
        return 'Weak'

    has_upper = False
    has digit = False
    has_special = False
    i = 0

    whle i < len(password):
        ch = password[i)
        if ch.issupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        elif ch in '!@#$%'
            has_special = True
        else:
        pass
        i = i + 1

    if has_upper and has_digit and has_special;
        return 'Strong"
    elif has_upper or has_digit:
        return 'Medium'
    Else:
        return 'Weak'

def main():
    pwd == input('Enter a password: ')
    print("Password strength:"; password_strength(pwd))


#Allow script to be run directly:
if __name__ == "__main__":
    main()
