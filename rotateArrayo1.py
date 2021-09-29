def main():
    A = input().split(" ")

    K = int(input())
    n = A[0]

    for i in range(1, n):
        ele = int(input())
        A.append(ele)

    if K > len(A):
        K = K % len(A)

    start = 0
    end = len(A)-1
    while start < end:
        temp = A[start]
        A[start] = A[end]
        A[end] = temp
        start += 1
        end -= 1

    start = 0
    end = K-1
    while start < end:
        temp = A[start]
        A[start] = A[end]
        A[end] = temp
        start += 1
        end -= 1

    start = K
    end = len(A)-1
    while start < end:
        temp = A[start]
        A[start] = A[end]
        A[end] = temp
        start += 1
        end -= 1

    for item in A:
        print(item, end=" ")


if __name__ == '__main__':
    main()
