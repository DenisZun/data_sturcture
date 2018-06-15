def bubble(list):
    """python冒泡排序"""
    n = len(list)
    for i in range(1, n):
        for j in range(1, n - i + 1):
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
    return list

if __name__ == '__main__':
    list_01 = [1, 32, 12, 54, 46, 554, 334, 2000423]
    print(bubble(list_01))
