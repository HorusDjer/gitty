"""

Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
"""

def order(sentence):
    result = []
    temp = []
    for word in sentence.split():
        for letter in word:
            if letter.isdigit():
                index = int(letter)
                temp.append((index, word))
    temp.sort(key=lambda index: (index, word))
    for pair in temp:
        result.append(pair[1])
    
    return ' '.join(result)

sentence = "Thi1s is2 3a T4est"

print(order(sentence))