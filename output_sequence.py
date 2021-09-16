def output_sequence(amount):
    sequence = ''
    for i in range(amount + 1):
        for j in range(i + 1):
            sequence += str(j)
            print(j, end='')
        if i != amount:
            sequence += '\n'
        print()
    return sequence
