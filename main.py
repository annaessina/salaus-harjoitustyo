
#This function encrypts given message (empty at this moment)
def encrypt(message):

    return message

#This function decrypts given message (empty at this moment)
def decrypt(message):

    return message


# Start
def start():
 
    print("This program encrypts and decrypts messages using RSA algorithm.\n")
    print("Choose an option below: \n")
    print("To generate public and private keys, type in 1")
    print("To encrypt message from terminal, type in 2")
    print("To decrypt message from terminal, type in 3")
    print("To encrypt message from file, type in 4")
    print("To decrypt message from file, type in 5")

    while True:

        # Get selection from user
        option = input()

        # Generate public and private keys
        if option == "1":
            print()

        # Encrypt message from terminal
        elif option == "2":
            print()

        # Decrypt message from terminal
        elif option == "3":
            print()

        # Encrypt message from file
        elif option == "4":
            print()

        # Decrypt message from file
        elif option == "5":
            print()

        # Check, if input is invalid
        else:
            print("Such option does not exist\n")

        # Option to exit  
        print("Make another choice?\n\
        'y' to continue, 'n' to exit\n")
        quit = input()  

        # If 'y' is chosen
        if quit == "y":
            continue
        # If 'n' is chosen
        else:
            break

 
if __name__ == "__main__":
    start()
