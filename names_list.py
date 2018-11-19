# https://www.codewars.com/kata/format-a-string-of-names-like-bart-lisa-and-maggie/python

def namedlist(names):
    # my answer lol
    if len(names) < 1:
        return ''
    elif len(names) == 1:
        return names[0]['name']
    elif len(names) == 2:
        return '{} & {}'.format(names[0]['name'], names[1]['name'])
    else:
        temp = ['{},'.format(descrip['name']) for descrip in names]
        temp.insert(-1, '&')
        result = []
        for char in temp:
            if char == temp[-3] or char == temp[-1]:
                char = char.replace(',', '')
            result.append(char)
        return ' '.join(result)


# better answer
def namelist(names):
    name_str = ''                                  
    if (len(names) > 0):
        for i in range(0,len(names)):
            if (i == len(names) - 1 and i > 0):
                name_str += " & "
            elif (i > 0):
                name_str += ", "
            name_str += names[i]['name']

    return name_str