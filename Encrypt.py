import random


class Encrypt:

    def __init__(self, message):
        self.message = message


    def Encryption(self):
        MessageListBin = []
        MessageListChar = []
        Message = self.message

        for i in Message: #Turns the strings into binary and puts them into a list
            ordOfLetter = ord(i) #This gives the unicode number of the char
            bina = bin(ordOfLetter)[2:]
            if (len(bina) == 7):
                MessageListBin.append(bina)
            elif (len(bina) == 6): #This is to fix space that is 6 bit for some reason
                bina = "0" + bina
                MessageListBin.append(bina)



        for i in MessageListBin: #Makes the 0's random numbers and the 1's random letters.
            for j in range(len(i)):
                currentNumberInJ = i[j]
                if (currentNumberInJ == "0"):
                    randomNumber = random.randint(48, 57)
                    MessageListChar.append(randomNumber)    
                elif (currentNumberInJ == "1"):
                    randomNumber = random.randint(97, 122)
                    MessageListChar.append(randomNumber)


        eWrite = open("EncryptedMessage.txt", "w")
        eWrite.truncate(0)
        for chars in MessageListChar:
            ucodeNumToString = chr(chars)
            eWrite.write(ucodeNumToString)
        print("Your message has been encrypted!")

    
    def Decryption(self): # Every char is 7 bits exept space which is 6 bits
        listOfSepatateChars = []
        listOfSepatateBin = []
        listOfGroupedBin = []
        listOfUnicodeNumber = []
        listOfLetters = []
        for i in self.message:
            listOfSepatateChars.append(i)

        for i in listOfSepatateChars:
            if i.isalpha():
                listOfSepatateBin.append(1)
            else:
                listOfSepatateBin.append(0)

        for i in range(len(listOfSepatateBin)//7): #This groups the bin chars to a string that we can later convert to Unicode (code) which we will convert to string
            tempBinAssigner = ""
            for j in range(7):
                tempBinAssigner = tempBinAssigner + str(listOfSepatateBin[0])
                listOfSepatateBin.pop(0)
            if(len(tempBinAssigner)==7):
                listOfGroupedBin.append(tempBinAssigner)
            elif(len(tempBinAssigner) == 6):
                listOfGroupedBin.append("1"+tempBinAssigner)
        
        for bin in listOfGroupedBin:
            listOfUnicodeNumber.append(int(bin, 2))

        for nums in listOfUnicodeNumber:
            listOfLetters.append(chr(nums))
        
        Writer = open("DecryptedMessage.txt", "w")
        Writer.truncate(0)

        for letters in listOfLetters:
            Writer.write(letters)

        print("Your message has been decrypted!")

        




        
