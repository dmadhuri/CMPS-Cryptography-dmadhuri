###############################################
# Name: Vijaya Madhuri Devarapalli
# Class: CMPS 4664 Cryptography
# Date: 26 July 2015
# Program 2 - Randomized Vigenere Cipher
###############################################

import argparse
from randomized_vigenere import Vigenere

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", dest="mode", default = "encrypt", help="Encrypt or Decrypt")
    parser.add_argument("-i", "--inputfile", dest="inputFile", default = "inputFile.txt", help="Input Name")
    parser.add_argument("-o", "--outputfile", dest="outputFile", default = "outputFile.txt", help="Output Name")
    parser.add_argument("-s", "--seed", dest="seed", default =12001907, help="Integer seed")
    args = parser.parse_args()
    seed = int(args.seed)

    #open input file
    f = open(args.inputFile,'r')
	#reading message from input file
    message = f.read()
	#Constructing VigenereMatrix
    VigenereMatrix = Vigenere(seed)
    VigenereMatrix.setPlain_text_message(message)

	#Check if the mode is encrypt or not
    if(args.mode == 'encrypt'):
        encryptedText = VigenereMatrix.encrypt()
        o = open(args.outputFile,'w')
		
        o.write("""###############################################
        # Name: Vijaya Madhuri Devarapalli
        # Class: CMPS 4664 Cryptography
        # Date: 27 July 2015
        # Program 2 - Randomized Vigenere Cipher
        ###############################################\n""")

        o.write('KeyWord is:' + VigenereMatrix.keyWord)
        o.write('\n Plain text Message is:' + message)
        o.write('\n Encrypted Message is:' + encryptedText)

    else:
        
        decryptedText = VigenereMatrix.decrypt()
        o = open(args.outputFile,'w')
        o.write("""###############################################
        # Name: Vijaya Madhuri Devarapalli
        # Class: CMPS 4664 Cryptography
        # Date: 27 July 2015
        # Program 2 - Randomized Vigenere Cipher
        ###############################################\n""")
        
       
        o.write('KeyWord is:' + VigenereMatrix.keyWord)
        o.write('\n Encrypted text Message is:' + message)
        o.write('\n Decrypted Message is:' + decryptedText)
		
	#closing file	
    f.close()
	
if __name__ == '__main__':
    main()
	
