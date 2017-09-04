def show():
    top = 3
    shw = 1
    facedown = 15
    total = 52
    den = total - top - shw
    num = top * 8

    fact1 = (num / den * (facedown - 1) * 1000) + 5000

    print(fact1)

    n = den - num
    d = den
    for i in range(2, facedown):
        fact = 1
        for j in range(0, i-1):
            fact = fact * (n - j) / (d - j)

        fact0 = (facedown - top - shw) / (d - i + 1)
        fact = (fact * fact0 * ((facedown - i) * 1000) + 5000)
        print(fact)
