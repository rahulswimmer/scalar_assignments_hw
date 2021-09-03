package main

import "fmt"

func main() {
	inputArr := []int{8, 15, 1, 10, 5, 19, 19, 3, 5, 6, 6, 2, 8, 2, 12, 16, 3}
	fmt.Println(solve(inputArr))
}

func solve(A []int) int {
	duplicateArr := []int{}
	inputMap := make(map[int]int)
	for i := 0; i < len(A); i++ {
		inputMap[A[i]] += 1
	}
	fmt.Println(inputMap)
	for key, value := range inputMap {
		if value > 1 {
			duplicateArr = append(duplicateArr, key)
		}
	}
	if len(duplicateArr) == 0 {
		return -1
	} else {
		return duplicateArr[0]
	}
}
