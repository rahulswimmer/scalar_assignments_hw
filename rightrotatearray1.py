def rightRotate(lists, num):
    output_list = []

    # Will add values from n to the new list
    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])

    # Will add the values before
    # n to the end of new list
    for item in range(0, len(lists) - num):
        output_list.append(lists[item])

    for i in range(0, len(lists)-1):
        print(lists[i]),


# Driver Code
rotate_num = 3
list_1 = [1, 2, 3, 4, 5]
