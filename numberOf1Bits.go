package main

import "fmt"

func main() {
	input := 6
	fmt.Println(numSetBits(input))
}

func numSetBits(A int) int {
	count := 0
	for A != 0 {
		count += A & 1
		A >>= 1
	}
	return count
}
