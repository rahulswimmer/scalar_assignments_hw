package main

import "fmt"

func main() {
	arr := []int{1, 3, 56, -9, 59, -89}
	fmt.Println(solve(arr))
}

func solve(a []int) int {
	max, min := a[0], a[0]
	for _, value := range a {
		if max < value {
			max = value
		}
		if min > value {
			min = value
		}
	}
	tempArr := []int{}
	for _, value := range a {
		if value != max && value != min {
			tempArr = append(tempArr, value)
		}
	}
	return len(tempArr)

}
