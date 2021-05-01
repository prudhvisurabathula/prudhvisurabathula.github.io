def main():
    full_name = get_full_name()
    print()
    password = get_password()
    print()
    email_address = get_email_address()
    print()
    phone_number = get_phoneno()
    print()
    print("Hi " + full_name.split()[0], "thanks for creating an account.")
    print("we'll text your confirmation code to this number:", phone_number)


def get_full_name():
    while True:
        name = input("Enter full name:").strip()
        if " " in name:
            return name

def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print("Password must be 8 characters or more \n" +
                  "with at least one digit and one uppercase letter.")
        else:
            return password

def get_email_address():
    import re
    while True:
        str = input("enter the email address:")
        m = re.match(r'(^[a-z][0-9a-zA-Z]+[@][a-z]+[0-9A-Za-z]+\.com)', str, re.M)
        if m:
            return m.group()

        else:
            print("please enter valid email address")

def get_phoneno():
    while True:

        phone = input("Enter phone number:").strip()
        cell = ""
        for char in phone:
            if not char == "(" and not char == ")" and not char == " " and not char == "-":
                cell = cell + char

        if not cell.isdigit() or len(cell) != 10:
            print("Please enter a 10-digit phone number.")
        else:
            cell = cell[:3] + "." + cell[7:] + "." + cell[6:]
            return cell

if __name__ == "__main__":
    main()
