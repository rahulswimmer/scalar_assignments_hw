package main

import "fmt"

func main() {
	arr := []int{-15, -45, 43, 23, -63, 69, 35, 19, 37, -52}
	solve(arr)

}

func solve(A []int) int {
	max1 := 0
	max2 := 1

	for _, value := range A {
		if value%2 != 0 {
			max2 = value
			break
		}
	}

	for _, value := range A {
		if value%2 == 0 {
			max1 = value
			break
		}
	}

	fmt.Println(max2)
	for _, value := range A {
		if value%2 == 0 {
			if max1 < value {
				max1 = value
			}
		} else {
			if max2 > value {
				max2 = value
			}
		}
	}
	fmt.Println(max2)
	fmt.Println(max1)
	return max1 - max2
}
