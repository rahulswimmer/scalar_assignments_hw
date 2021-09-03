package main

import (
	"fmt"
	"strconv"
)

func main() {
	n := 30
	fizzBuzz(n)
}

func fizzBuzz(A int) []string {
	outputArr := []string{}

	for i := 1; i <= A; i++ {
		if i%5 == 0 && i%3 == 0 {
			outputArr = append(outputArr, "FizzBuzz")
		} else if i%5 == 0 {
			outputArr = append(outputArr, "Buzz")
		} else if i%3 == 0 {
			outputArr = append(outputArr, "Fizz")
		} else {
			outputArr = append(outputArr, strconv.Itoa(i))
		}
	}
	fmt.Println(outputArr)
	return outputArr
}
