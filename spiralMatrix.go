package main

import "fmt"

func main() {
	arrLen := 3
	generateMatrix(arrLen)
}

func generateMatrix(A int) {
	a := [A][A]int{}
	for i := 0; i < A; i++ {
		for j := 0; i < A; j++ {
			a[i][j] = j
		}
	}

	fmt.Println(a)
}
