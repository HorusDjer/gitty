def minion_game(string):
    """a minion game"""
    letters = list(string.lower())
    consonants = []
    vowels = []
    all_vowels = ['a', 'e', 'i', 'o', 'u']
    
    for letter in letters:
        if letter in all_vowels:
            vowels.append(letter)
        else:
            consonants.append(letter)

    return vowels, consonants

if __name__ == '__main__':
    s = input('Enter your word here: ')
    print(minion_game(s))
