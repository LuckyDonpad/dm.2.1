def grey_code(n):
    a = [0 for i in range(n + 1)]
    j = 0
    while True:
        yield a[n - 1::-1]
        a[n] = 1 - a[n]
        if a[n] == 1:
            j = 0
        else:
            for i in range(n):
                if a[i] == 1:
                    j = i + 1
                    break
        if j >= n:
            return
        a[j] = 1 - a[j]


def subsets_generator(sequince):
    n = len(sequince)
    for code in grey_code(n):
        result = []
        for i in range(n):
            if code[i] == 1:
                result.append(sequince[i])
        if len(result) != 0:
            yield result
    return
