def main():
    arr = list(map(int, input().strip().split()[1:]))

    n = int(input())

    for i in range(0, n):
        l = arr[len(arr)-1]

        for j in range(len(arr)-1, -1, -1):
            arr[j] = arr[j-1]

        arr[0] = l
    for i in range(0, len(arr)):
        print(arr[i]),


if __name__ == '__main__':
    main()
