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

    def get_index_of_misc_chars(self, word):
        misc_chars = {}
        ''' this won't work because dictionary can't have multiple
        key, value pairs. I suggest a tuple or something else.'''
        for index, char in enumerate(word):
                misc_chars[char] = index
        
        return misc_chars

    def encode(self, word):
        word = word.lower()

        misc_char_positions = self.get_index_of_misc_chars(word)
        print(misc_char_positions)

        correct_positions = []
        for letter in word:
            for key, value in self.alphabet_values.items():
                if letter == key:
                    correct_position = value + self.shift
                    if correct_position > 26:
                        correct_position = correct_position - 26

                    correct_positions.append(correct_position)
        
        correct_letters = []
        for position in correct_positions:
            for key, value in self.alphabet_values.items():
                if position == value:
                    correct_letters.append(key)

        for key, value in misc_char_positions.items():
            correct_letters.insert(value, key)

        print(''.join(correct_letters).upper())


                    
    def decode(self, word):
        word = word.lower()

        misc_char_positions = self.get_index_of_misc_chars(word)

        correct_positions = []
        for letter in word:
            for key, value in self.alphabet_values.items():
                if letter == key:
                    correct_position = value - self.shift
                    if correct_position < 0:
                        correct_position = correct_position + 26

                    correct_positions.append(correct_position)

        correct_letters = []
        for position in correct_positions:
            for key, value in self.alphabet_values.items():
                if position == value:
                    correct_letters.append(key)

        for key, value in misc_char_positions.items():
            correct_letters.insert(value, key)

        print(''.join(correct_letters).upper())
        

c = CaesarCipher(5); # creates a CipherHelper with a shift of five
#c.encode('Codewars') # returns 'HTIJBFWX'
#c.decode('BFKKQJX') # returns 'WAFFLES'
c.encode('Cod ?ew [a$r  s')
