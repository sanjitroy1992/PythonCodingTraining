def countZeros(n):
    result = 0
    i = 1

    while True:
        b = n//i
        c = n % i
        # b, c = divmod(n, i)
        print("b, c : {}, {}".format(b, c))
        # a, b = divmod(b, 10)
        a = b // 10
        b = b % 10
        print("a, b : {}, {}".format(a, b))

        if a == 0:
            return result

        if b == 0:
            result += (a - 1) * i + c + 1
        else:
            result += a * i

        i *= 10

print(countZeros(10))