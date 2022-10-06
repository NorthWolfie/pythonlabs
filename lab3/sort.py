def BubbleSort(a):
    N = len(a)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def InsertionSort(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i - 1
        while j >= 0 and temp < a[j]:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = temp
    return a
