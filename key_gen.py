import sys
import random
import string


class VernamKeyGenerator:
    def __init__(self, length):
        self.length = length

    def generate(self):
        return self.__randomword()

    def __randomword(self):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(self.length))
length = len(open(sys.argv[1], 'r').read())
key = VernamKeyGenerator(length).generate()
f = open(sys.argv[2], 'w').write(key)

