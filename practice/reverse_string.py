def reverse_string(sentence):
    sentence = sentence[::-1]
    return sentence

def spin_words(sentence):
    answer = []
    index = -1
    for _ in sentence:
        answer.append(sentence[index])
        index -= 1
        
    return ''.join(answer)
    
def reverse_letters(sentence):
    new_list = list(sentence)
    # in place methods like list.reverse() return none.
    new_list.reverse()
    return ''.join(new_list)

def reversed_string(sentence):
    return ''.join(reversed(sentence))

sentence = 'Welcome, my friend. How are you today?'    
# print(reverse_string(sentence))
# print(spin_words(sentence))
print(reverse_letters(sentence))
print(reversed_string(sentence))