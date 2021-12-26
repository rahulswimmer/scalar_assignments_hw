def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = input()
    print(solve(A))
    
def solve(A):
    n = len(A)
    if n == 1:
        return A
    return A[n-1]+solve(A[:n-1])

if __name__ == '__main__':
    main()