import random
import string
import sys


class Key:

    def __init__(self, value):
        self.value = value

    def set(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def get_value(self):
        return self.value


class KeyVernam(Key):
    pass


class Crypto:

    def __init__(self, key):
        self.key = key

    def setKey(self, key):
        self.key = key

    def encrypt(self, string):
        pass

    def decrypt(self, string):
        pass


class CryptoVernam(Crypto):

    def encrypt(self, string):
        return self.__xor_string(string)

    def decrypt(self, string):
        return self.__xor_string(string)

    def __string_to_bytes(self, string):
        return bytes(string, 'utf-8')

    def __bytes_to_string(self, bytesList):
        print(bytesList)
        return "".join(map(chr, bytesList))

    def __xor_string(self, string):
        stringBytes = self.__string_to_bytes(string)
        keyBytes = self.__string_to_bytes(self.key.get_value())
        main_list = zip(keyBytes, stringBytes)
        bytes_list = list(map(lambda x: x[0] ^ x[1], main_list))
        return self.__bytes_to_string(bytes_list)


class CryptoManager:

    def __init__(self, crypto):
        self.crypto = crypto

    def encryptFile(self, inputFileName, outputFileName):
        return self.crypto.encrypt(string)

    def decryptFile(self, inputFileName, outputFileName):
        return self.crypto.decrypt(string)

    def encryptString(self, string):


    def decryptString(self, string):


content = open(sys.argv[2], 'r').read()
key = KeyVernam(open(sys.argv[3], 'r').read())
cm = CryptoManager(CryptoVernam(key))
outputFile = open(sys.argv[4], 'w')

if sys.argv[1] == '--decrypt':
    outputFile.write(cm.decryptFile(content))

elif sys.argv[1] == '--encrypt':
    outputFile.write(cm.encryptFile(content))
