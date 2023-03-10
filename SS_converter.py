def convert(n, osn):
    s = ''
    while n > 0:
        s += str(n % osn)
        n = n // osn
    return s[::-1]


print(int(convert(20, 14)) + int(convert(18, 13)))


x, y, z = (1, 11, 21, 31, 41, 51, 61, 71, 81)[1::3]
print(y)