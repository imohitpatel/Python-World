# Code source: https://github.com/imohitpatel/Python-World/edit/main/Complex%20User%20Interaction%20Password%20Generator/main.py
# Author : Mohit Patel (imohitpatel@Github)
# License: Custom license
import secrets
import string

def generate_password(password_len):
    if password_len < 8:
        raise ValueError("Password length must be at least 8 characters to include all required character types.")

    # Character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*"

    # Ensure at least one of each required character type
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special_chars)
    ]

    # Fill the rest of the password length with random choices from the selection list
    all_chars = lowercase + uppercase + digits + special_chars
    password += [secrets.choice(all_chars) for _ in range(password_len - 4)]

    # Shuffle to avoid predictable sequences
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

def main():
    try:
        print(":::::∆::∆::∆::> Welcome to the Password Generator <::∆::∆::∆:::::::")
        user_name = input("Please enter your name: ")
        print(f"Hello {user_name}! Let's generate some passwords.")

        while True:
            num_passwords = int(input("Enter the number of passwords you want: "))
            password_len = int(input("Enter the desired length of the password: "))

            if num_passwords < 1:
                raise ValueError("You must generate at least one password.")

            passwords = []
            for i in range(num_passwords):
                generated_password = generate_password(password_len)
                passwords.append(generated_password)
                print(f"Password {i + 1}: {generated_password}")

            while True:
                confirm_index = int(input("Enter the number of the password you want to confirm: ")) - 1

                if confirm_index < 0 or confirm_index >= num_passwords:
                    raise ValueError("Invalid password number.")

                confirmed_password = passwords[confirm_index]
                print(f"Confirmed password: {confirmed_password}")

                confirm_choice = input("Do you want to confirm this password? (yes/no): ").strip().lower()

                if confirm_choice == 'yes':
                    print("We appreciate your choice!")
                    break
                elif confirm_choice == 'no':
                    confirm_other_choice = input("Do you want to confirm another password choice? (yes/no): ").strip().lower()
                    if confirm_other_choice == 'yes':
                        continue
                    else:
                        break
                else:
                    print("Invalid choice. Please enter 'yes' or 'no'.")

            rerun_choice = input("Do you want to generate more passwords? (yes/no): ").strip().lower()

            if rerun_choice == 'no':
                print("Thank you for using the Password Generator, have a great day!")
                print("If you like this code, consider giving a star to this repository on GitHub: https://github.com/imohitpatel/python_world or visit the author account imohitpatel on Github")

                break

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
