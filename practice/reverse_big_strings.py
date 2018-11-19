def spin_words(sentence):
    list_of_words = sentence.split()
    
    if len(list_of_words) == 1:
        if len(list_of_words[0]) >= 5:
            list_of_words[0] = list_of_words[0][::-1]
            return list_of_words[0]
        else:
            return list_of_words[0]
    else:
        answer = []
        print('This is a list of words:', list_of_words)
        for word in list_of_words:
            if len(word) >= 5:
                word = word[::-1]
                answer.append(word)
            else:
                answer.append(word)
            print(answer)
        
        return ' '.join(answer)

sentence = """'thisandmorestringwilloneKataSpacessamefivebutbut' 
should equal 'this and more gnirts will one Kata secapS same five but but'"""

print(spin_words(sentence))