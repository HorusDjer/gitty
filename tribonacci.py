def tribonacci(signature, n):
    if n == 0:
        return []
    else:
        for num in range(n-3):
            next_num = signature[num] + signature[num + 1] + signature[num + 2]
            signature.append(next_num)
            
        return signature[n - 1]


signature = [1, 1, 1]
n = 10

print(tribonacci(signature, n))

def tribonaccii(signature, n):
    a, b, c = signature
    new_list = []
    for number in range(n):
        new_list.append(a)
        a, b, c = b, c, a+b+c
    
    return new_list