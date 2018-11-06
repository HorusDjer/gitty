def swap_case(s):
    pass


if __name__ == '__main__':
    s = input("Enter string: ")
    for letter in s:
        if letter == letter.lower():
            s.replace(letter, letter.upper())
        else:
            s.replace(letter, letter.lower())
    # result = swap_case(s)
    print(s)
