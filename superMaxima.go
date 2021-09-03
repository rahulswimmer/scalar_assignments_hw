package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	//size, _ := strconv.Atoi(scanner.Text())

	count := 0

	scanner.Scan()
	arr := strings.Split(scanner.Text(), " ")

	intarr := []int{}

	for _, i := range arr {
		j, _ := strconv.Atoi(i)
		intarr = append(intarr, j)
	}
	fmt.Println(len(intarr) - 2)
	for j := 1; j < len(intarr)-2; j++ {
		if intarr[j] > intarr[j-1] && intarr[j] > intarr[j+1] && intarr[j-1]+intarr[j+1] < intarr[j] {
			fmt.Println(intarr[j])
			count = count + 1
		}
	}

	fmt.Println(count)
}
