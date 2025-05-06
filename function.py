def ran(a, b):
    count = 0
    sum = 0

    for i in range(a + 1, b):
        print(i, end=",")
        count = count + 1
        sum = sum + i
    print()
    print("count =", count)
    print("Sum =", sum)


a = int(input())
b = int(input())
ran(a, b)
