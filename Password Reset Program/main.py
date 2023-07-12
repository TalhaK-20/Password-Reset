import pywhatkit


def password():
    print("  ****   Welcome to my Password Program ****   ")
    print("           Developed by TALHA KHALID")

    count = 0

    # with open('password.txt', 'w') as file:
    #     file.write("cool")

    with open('password.txt', 'r') as file:
        pass_word = file.read()

    a = str(input("Enter the Password Please = "))

    while a != pass_word:
        count = count + 1
        print("OOPS! It's the wrong password......")
        a = str(input("Enter the Password again = "))

        if count > 2:
            print("Dear! I think that you've forgotten your password")
            print("Do you want to reset ? If yes, press 'y' and if no, press 'n'")
            b = str(input("Enter the option Please = "))

            while b != "y" and b != "Y" and b != "n" and b != "N":
                b = str(input("Enter a valid option Please = "))

            if b == 'y' or b == 'Y':
                pywhatkit.sendwhatmsg_instantly("+923070282493", "Dear user, you've requested to change"
                                                                 " your password for the application.")

                pass_word = str(input("Enter the new Password Please = "))
                print("Your password has been changed")

                pywhatkit.sendwhatmsg_instantly("+923070282493", "Dear user, your password for"
                                                                 " the application has been changed.")

                with open('password.txt', 'w') as file:
                    file.write(pass_word)

                with open('password.txt', 'r') as file:
                    pass_word = file.read()

                a = str(input("Enter the New Password to login = "))

            if b == 'n' or b == 'N':
                a = str(input("Enter the Password again = "))

    print("Welcome to my coding world !")


password()
