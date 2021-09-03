package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	n, _ := strconv.ParseInt(scanner.Text(), 10, 64)
	solve(int(n))
}

func solve(A int) {
	op := [][]int{}
	for i := 1; i <= int(A); i++ {
		for j := 1; j <= i; j++ {
			op[i][j] = j
		}
	}
	fmt.Println(op)
}
