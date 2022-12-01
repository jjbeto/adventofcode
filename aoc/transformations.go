package aoc

import (
	"strconv"
)

func ToIntBase10(text string) int {
	number, err := strconv.ParseInt(text, 10, 0)
	if err != nil {
		panic(err)
	}
	return int(number)
}

func ToIntBase2(text string) int {
	number, err := strconv.ParseInt(text, 2, 0)
	if err != nil {
		panic(err)
	}
	return int(number)
}

func ToString(text string) string {
	return text
}
