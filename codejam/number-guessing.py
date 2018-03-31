def get_guess(lb, geb):
    g = (lb + geb) // 2
    if g == lb:
        g = lb + 1
    return g


t = int(input())
for _ in range(t):
    a, b = tuple(map(int, input().split()))
    n = int(input())

    lower_bound = a
    greater_equal_bound = b

    while True:
        g = get_guess(lower_bound, greater_equal_bound)
        print(str(g))

        response = input()
        n -= 1
        if response == "CORRECT":
            break
        elif response == "TOO_SMALL":
            lower_bound = g
        elif response == "TOO_BIG":
            greater_equal_bound = g - 1
        elif response == "WRONG_ANSWER":
            break
