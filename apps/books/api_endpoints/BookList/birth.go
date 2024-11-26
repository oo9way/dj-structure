package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Print("Enter your birth date in this formart 'YYYY-MM-DD': ")

	var input string
	_, err := fmt.Scan(&input)
	if err != nil {
		fmt.Println("Error reading input:", err)
		return
	}

	layout := "2006-01-02"

	birthDate, err := time.Parse(layout, input)

	if err != nil {
		fmt.Println("Invalid date format. Please use YYYY-MM-DD.")
		return
	}

	fmt.Println("Your birth date is:", birthDate.Format(layout))
}
