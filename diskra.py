def find_truth_table():
    a = []
    for i in range(2 ** 5):
        b = bin(i)[2:].zfill(5)
        x1x3x4 = f'{b[0]}{b[2]}{b[3]}'
        x1x3x4_10 = int(x1x3x4, 2)
        edx2x5 = f'1{b[1]}{b[4]}'
        edx2x5_10 = int(edx2x5, 2)
        minus = x1x3x4_10 + edx2x5_10
        f = 'd' if x1x3x4_10 == 7 else '1' if 8 <= minus < 12 else '0'
        a.append([b, x1x3x4, x1x3x4_10, edx2x5, edx2x5_10, minus, f])
    with open('truth_table.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join('\t'.join(str(i) for i in l) for l in a))
    print('Written in truth_table.txt')
    return {i[0]: i[-1] for i in a}


def glue(a, b):
    k = 0
    ii = -1
    for i in range(len(a)):
        if a[i] != b[i]:
            k += 1
            ii = i
    if k == 1:
        if a[ii] != 'X' and b[ii] != 'X':
            return a[:ii] + 'X' + a[ii + 1:]


def find_Z(a):
    z = []

    k = []
    k.append([[b, ''] for b, f in a.items() if f != '0'])
    k[-1].sort(key=lambda x: x[0].count('1'))
    v = {666}
    while v:
        v = set()
        k.append([])
        for i in range(len(k[-2])):
            for j in range(i + 1, len(k[-2])):
                _glue = glue(k[-2][i][0], k[-2][j][0])
                if _glue:
                    if _glue not in [p[0] for p in k[-1]]:
                        k[-1].append([_glue, f'{i + 1}-{j + 1}'])
                    else:
                        for p in range(len(k[-1])):
                            if k[-1][p][0] == _glue:
                                k[-1][p][1] = f'{k[-1][p][1]} {i + 1}-{j + 1}'
                                break
                    v.update([i, j])
        for i in range(len(k[-2])):
            if i not in v:
                z.append(k[-2][i][0])
        for i in range(len(k[-2])):
            print(f'{f"{i + 1}.":<4}{k[-2][i][0]} {"v" if i in v else " "}  {k[-2][i][1]}')
        print()

    print(*z, sep='\n')
    return z


a = find_truth_table()
Z = find_Z(a)