def valid_parentheses(string):
    chars = list(string)
    parentheses = list()
    for char in chars:
        if char == '(' or char == ')':
            parentheses.append(char)        
    
    if len(parentheses) == 1:
        return False
    if len(parentheses) == 0:
        return True
    elif parentheses[0] == ')' or parentheses[-1] == '(':
        return False
    elif parentheses.count(')') == parentheses.count('('):
            return True
    else:
        return False


string =  '(cdmm)jh((b)uu'
print(valid_parentheses(string))

# better answer below

def validate_parentheses(string):
    count = 0
    for i in string:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0