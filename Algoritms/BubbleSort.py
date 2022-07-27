my_list = [10, 15, 25, 11, 48, -52, 14]


def bubble_sort(my_list):
    last_item = len(my_list) - 1
    for i in range(0, last_item):
        for x in range(0, last_item-i):
            if my_list[x] > my_list[x+1]:
                my_list[x], my_list[x+1] = my_list[x+1], my_list[x]
    return my_list


print("Old list: ", my_list)
sort_list = bubble_sort(my_list).copy()
print("New list: ", sort_list)
