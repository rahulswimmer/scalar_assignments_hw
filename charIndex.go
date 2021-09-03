package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()

	input := strings.Fields(scanner.Text())

	fmt.Println([]rune(input))

	// for i, value := range input {
	// 	output = append(output, value)
	// 	output = append(output, strconv.Itoa(i))
	// }

	// fmt.Println(output)
}
