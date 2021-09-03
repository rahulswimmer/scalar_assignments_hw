package main

import "fmt"

func main() {
	inputArr := []int{1, 2, 3, 4}
	fmt.Println(solve(inputArr, 66))
}

func solve(A []int, B int) int {
	goodPairCount := 0
	for i := 0; i < len(A); i++ {
		for j := i + 1; j < len(A); j++ {
			if i != j && (A[i]+A[j] == B) {
				goodPairCount += 1
			}
		}
	}
	return goodPairCount
}
