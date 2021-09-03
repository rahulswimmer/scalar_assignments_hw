package main

import "fmt"

func main() {
	inputArr1 := []int{1, 2, 2, 1}
	inputArr2 := []int{2, 3, 1, 2}
	fmt.Println(solve(inputArr1, inputArr2))
}

func solve(A []int, B []int) []int {
	duplicateArr := []int{}
	inputMap := make(map[int]int)
	for i := 0; i < len(A); i++ {
		inputMap[A[i]] += 1
	}
	fmt.Println(inputMap)

	for i := 0; i < len(A); i++ {
		for j := 0; j < len(B); j++ {
			if A[i] == A[j] {
				duplicateArr = append(duplicateArr, A[i])
				break
			}
		}
	}
	return duplicateArr
}
