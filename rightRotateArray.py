def main():
    # a = [list(map(int, input().strip().split()[1:]))]
    # d = int(input())

    a = []

    d = int(input())
    n = int(input())
    for _ in range(0, n):
        ele = int(input())
        a.append(ele)

    output_list = []

    for item in range(len(a) - d, len(a)):
        output_list.append(a[item])

    for item in range(0, len(a) - d):
        output_list.append(a[item])


main()
