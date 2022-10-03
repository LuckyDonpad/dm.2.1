def placements(n, k):
    placement = [0 for i in range(k)]
    while True:
        yield (placement)
        for i in range(k - 1, -1, -1):
            if placement[i] < n - 1:
                break
        else:
            return
        placement[i] += 1
        for j in range(i + 1, k):
            placement[j] = 0
