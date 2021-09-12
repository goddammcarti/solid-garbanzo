def buble_sort(l):
    t = l.copy()
    for n in range(len(t)):
        for i in range(len(t) - n):
            if i < (len(t) - n) - 1 and t[i] > t[i+1]:
                t[i], t[i+1] = t[i+1], t[i]
    return t

nums = [4, 1, 6, 3, 2, 7, 8, -3]

sorted = buble_sort(nums)
print(sorted)

#ошибка то, что нужно сравнивать соседние элементы t[n] нужно заменить на t[i + 1],
