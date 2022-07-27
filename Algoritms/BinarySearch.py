my_list = [10, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 79, 81]
start = 0
stop = len(my_list)
find = 15


def binary_search(my_list, find, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if find == my_list[mid]:
            return mid
        elif find < my_list[mid]:
            return binary_search(my_list, find, start, mid - 1)
        else:
            return binary_search(my_list, find, mid + 1, stop)


x = binary_search(my_list, find, start, stop)

if not x:
    print("Item ", find, "not found!")
else:
    print("Item ", find, "found at index: ", x)
