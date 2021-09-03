package main

import "fmt"

func main() {
	arr := []int{1, 2, 3, 4, 4, 3, 1, 2, 676}
	fmt.Println(singleNumber(arr))
}

func singleNumber(A []int) int {
	x := 0
	for _, value := range A {
		x = x ^ value
	}

	return x
}
