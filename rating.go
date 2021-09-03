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
	rating, _ := strconv.ParseInt(scanner.Text(), 10, 64)

	outputRating := ""
	if rating <= 2500 && rating >= 1000 {
		switch {
		case rating >= 2100:
			outputRating = "grand master"
		case rating >= 1900:
			outputRating = "candidate master"
		case rating >= 1600:
			outputRating = "expert"
		case rating >= 1400:
			outputRating = "pupil"
		case rating < 1400:
			outputRating = "newbie"
		default:
			fmt.Println("no rating exists for ", rating)
		}
		if rating%2 == 0 {
			fmt.Println(strings.ToUpper(outputRating))
		} else {
			fmt.Println(outputRating)
		}

	} else {
		fmt.Println("Input should be between 1000 and 2500.")
	}

}
