import string

class CaesarCipher(object):
    
    def __init__(self, shift):
        self.shift = shift
        self.alphabet = string.ascii_lowercase
        self.alphabet_values = {}
        
        x = 1
        for letter in self.alphabet:
            self.alphabet_values[letter] = x
            x += 1

    def encode(self, word):
        word.lower()
        correct_letters = []
        for letter in word:
            for key, value in self.alphabet_values.items():
                if letter == key:
                    correct_position = value + 5
                    correct_letters.append(correct_position)
        
        print(correct_letters) 
                    
    def decode(self, str):
        pass;
        

c = CaesarCipher(5); # creates a CipherHelper with a shift of five
c.encode('Codewars') # returns 'HTIJBFWX'
# c.decode('BFKKQJX') # returns 'WAFFLES'
