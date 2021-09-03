package main

import "fmt"

func main() {
	inputArray := []int{1, 2, 2, 5, 6}
	solve(inputArray)

}

func solve(A []int) int {
	outputArr := []int{}
	for i := 0; i < len(A); i += 2 {
		if A[i]%2 != 0 && A[i+1]%2 == 0 {
			outputArr = append(outputArr, A[i])
		} else {
			outputArr = append(outputArr, A[i+1])
		}
	}
	fmt.Println(outputArr)
	return 0
}
