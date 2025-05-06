def bits(x, y):
    times = 10

    while times > 0:
        print(x & 1, x)
        x <<= 1
        times -= 1

    times = 10
    print()
    while times > 0:
        print(y & 1, y)
        y >>= 1
        times -= 1


bits(10, 7168)
