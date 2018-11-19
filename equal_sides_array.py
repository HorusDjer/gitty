def find_even_index(arr):
    if len(arr) == 1:
        return 0
    else:
        for number in range(len(arr)):
            if sum(arr[:number]) == sum(arr[number + 1:]):
                return number
                
    return -1


arr = [20,10,30,10,10,15,35]
print(find_even_index(arr))