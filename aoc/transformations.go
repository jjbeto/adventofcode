package aoc

import (
	"strconv"
)

func ToIntBase10(text string) int64 {
	number, err := strconv.ParseInt(text, 10, 0)
	if err != nil {
		panic(err)
	}
	return number
}

func ToIntBase2(text string) int64 {
	number, err := strconv.ParseInt(text, 2, 0)
	if err != nil {
		panic(err)
	}
	return number
}

func ToString(text string) string {
	return text
}
