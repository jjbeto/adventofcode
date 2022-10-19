package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/helper"
)

func part1(numbers []int64) int64 {
	var prev, increases int64 = -1, 0
	for i, next := range numbers {
		if prev < next && i > 0 {
			increases++
		}
		prev = next
	}
	return increases
}

func part2(numbers []int64) int64 {
	var rolling []int64
	for i := 0; i <= len(numbers)-2; i++ {
		rolling = append(rolling, helper.Sum(numbers[i:i+3]))
	}
	return part1(rolling)
}

func main() {
	numbers := helper.ReadNumbers("2021", "day01.data", 10)
	fmt.Println(part1(numbers))
	fmt.Println(part2(numbers))
}
