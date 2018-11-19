def isValidWalk(walk):
    x, y = 0, 0
    if len(walk) < 10 or len(walk) > 10:
        return False
    else:
        for direction in walk:
            if direction == 'n':
                y += 1
            if direction == 's':
                y -= 1
            if direction == 'e':
                x += 1
            if direction == 'w':
                x -= 1
                
    if x == 0 and y == 0:
        return True
    else:
        return False