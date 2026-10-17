
import string


def check_password_strength(password):
    checks = {
        "At least 8 characters": len(password) >= 8,
        "At least 12 characters": len(password) >= 12,
        "Contains uppercase letters": any(c.isupper() for c in password),
        "Contains lowercase letters": any(c.islower() for c in password),
        "Contains numbers": any(c.isdigit() for c in password),
        "Contains symbols": any(c in string.punctuation for c in password),
    }

    score = sum(checks.values())

    if len(password) < 8:
        strength = "Weak"
    elif len(password) >= 12 and score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, checks


def main():
    print("=" * 40)
    print("     PASSWORD STRENGTH CHECKER")
    print("=" * 40)

    password = input("Enter a fictional test password: ")

    strength, checks = check_password_strength(password)

    print("\nPassword Strength:", strength)
    print("\nSecurity Checks:")

    for check, passed in checks.items():
        result = "PASS" if passed else "NOT MET"
        print(f"{check}: {result}")

    print("\nTip: Use a long, unique password.")
    print("This result is a basic educational estimate.")


if __name__ == "__main__":
    main()
