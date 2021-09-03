def test():
    st = 'Print only the words that start with s in this sentence'
    for value in st.split(" "):
        if value[0] == "s":
            print(value)

    for value in range(0, 10):
        print(value)

    list1 = [num for num in range(1, 50) if num % 3 == 0]
    print(list1)


test()
