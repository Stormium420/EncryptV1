from Encrypt import Encrypt

Chosen = False #While user hasnt chosen a correct option

print("""
   _____ _                       _                 
  / ____| |                     (_)                
 | (___ | |_ ___  _ __ _ __ ___  _ _   _ _ __ ___  
  \___ \| __/ _ \| '__| '_ ` _ \| | | | | '_ ` _ \ 
  ____) | || (_) | |  | | | | | | | |_| | | | | | |
 |_____/ \__\___/|_|  |_| |_| |_|_|\__,_|_| |_| |_| """)

while Chosen == False:
    print(
        ("""
OPTIONS
    
1) Encrypt
2) Decrypt
    """)
    )

    option = input("Enter your choice: ")



    if (option == "1"):
        Chosen = True
        message = input("Enter your message: ")
        Runner = Encrypt(message)
        Runner.Encryption()
    elif (option == "2"):
        Chosen = True
        message = input("Enter your encrypted message: ")
        Runner = Encrypt(message)
        Runner.Decryption()
    else:
        print("Not an option, chose again\n\n")

input("\n\nPress enter to exit.")
