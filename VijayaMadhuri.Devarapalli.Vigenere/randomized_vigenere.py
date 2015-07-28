import random

class Vigenere:

    #Initialize Vigenere object.
    def __init__(self, seed):
        random.seed(seed)
        self.seed = seed
        self.chars= """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""
        self.Vigenere_Table = [[0 for i in range(len(self.chars))] for i in range(len(self.chars))]
        self.keyWord = ""
        self.plain_text_message = ""
        self.cipher_text_message = ""
        self.keywordFromSeed(seed)
        
    def setPlain_text_message(self,plain_text_message):
        self.plain_text_message = plain_text_message	
    
	#Printing Matrix
    def printMatrix(self):
        i = 0
        j = 0
        k = 0
        line = ""
        for i in range(95*95):
            line = line + self.Vigenere_Table[j][k]
            j = j+1
            if j >= 95:
                print(line)
                line = ""
                j = 0
                k = k+1
                    
    #Generate psuedorandom keyword from seed
    def keywordFromSeed(self,seed):
        Letters = []

        while seed > 0:
            Letters.insert(0,chr((seed % 100) % 26 + 65))
            seed = seed // 100
        self.keyWord = "".join(Letters)
        self.buildVigenere()

    #Building random Vigenere Table
    def buildVigenere(self):
        random.seed(self.seed)
        temp = list(self.chars)
        random.shuffle(temp)
        temp = ''.join(temp)

        for sym in temp:
            random.seed(self.seed)
            vigenereList = []
            for i in range(len(temp)):
                r = random.randrange(len(temp))
                if r not in vigenereList:
                    vigenereList.append(r)
                else:
                    while(r in vigenereList):
                        r = random.randrange(len(temp))
                    vigenereList.append(r)
                while(self.Vigenere_Table[i][r] != 0):
                    r = (r + 1) % len(temp)
                self.Vigenere_Table[i][r] = sym
    
	#Encrypting Plain Text Message by passing the message index and key index and by getting the ascii values of 
	#characters and display the corresponding character based on the particular row and column
    def encrypt(self):
        for index in range(len(self.plain_text_message)):
            message_index = index
            key_index = index % len(self.keyWord)
            self.cipher_text_message = self.cipher_text_message + self.getEncrypted(key_index,message_index)
        return self.cipher_text_message

    def getEncrypted(self,key_index,message_index):       
        row = ord(self.plain_text_message[message_index]) - 32
        col = ord(self.keyWord[key_index]) - 32
        return self.Vigenere_Table[row][col]

	#Decrypting Encrypted Text Message by passing the message index and key index and getting the ascii value 
	#of each character and adding to the final message
    def decrypt(self):
        self.cipher_text_message = ""
        for index in range(len(self.plain_text_message)):
            encrypted_message_index = index
            key_index = index % len(self.keyWord)
            self.cipher_text_message = self.cipher_text_message + self.getDecrypted(key_index,encrypted_message_index)
        return self.cipher_text_message

    def getDecrypted(self,key_index,encrypted_message_index):
        
        size = len(self.chars)
        col = ord(self.keyWord[key_index]) - 32
        for row in range(size):
            if self.Vigenere_Table[row][col] == self.plain_text_message[encrypted_message_index]:
                char = chr(row + 32)
                return(char)
				
				
