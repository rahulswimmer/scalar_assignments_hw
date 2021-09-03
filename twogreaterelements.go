package main

import "fmt"

func main() {
	arr := []int{1, 2, 3, 4, 5}
	fmt.Println(solve(arr))
}

func solve(a []int) []int {
	max := a[0]
	for _, value := range a {
		if max < value {
			max = value
		}
	}
	tempArr := []int{}
	for _, value := range a {
		if value != max {
			tempArr = append(tempArr, value)
		}
	}
	secondMax := tempArr[0]
	for _, value := range tempArr {
		if secondMax < value {
			secondMax = value
		}
	}
	tempArr1 := []int{}
	for _, value := range tempArr {
		if value != secondMax {
			tempArr1 = append(tempArr1, value)
		}
	}

	return tempArr1

}
