def fizzbuzz():
    outputArr = []
    n = 30
    for value in range(1, n+1):
        if value % 3 == 0 and value % 5 == 0:
            outputArr.append("FizzBuzz")
        elif value % 3 == 0:
            outputArr.append("Fizz")
        elif value % 5 == 0:
            outputArr.append("Buzz")
        else:
            outputArr.append(value)
    print(outputArr)


fizzbuzz()
