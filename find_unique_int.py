
# fast attempt O(N)
def find_uniq(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for num in arr:
        if counts[num] == 1:
            return num

# bad attempt  O(n^2)
def find_uniq_(arr):
    for num in arr:
        if arr.count(num):
            return num

def find_unique(arr):
    s = set(arr)
    for e in s:
        if arr.count(e) == 1:
            return e