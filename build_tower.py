def tower_builder(n_floors):
    answer = []
    stars = '*'
    factor = 1

    for i in range(n_floors):
        block = (i + factor) * stars
        padded_block = '{:^{x}}'.format(block, x=(i + 1))
        answer.append(padded_block)
        factor += 1

    return answer


n_floors = 3

print(tower_builder(n_floors))

# (0 + 1) * x = 1
# (1 + 2) * x = 3
# (2 + 3) * x = 5

