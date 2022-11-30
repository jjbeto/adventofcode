package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
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
	return part1(aoc.SlidingWindow(aoc.Sum[int64], numbers, 3))
}

func main() {
	numbers := aoc.ReadLines("2021/day01", "data.txt", aoc.ToIntBase10)
	fmt.Println("part1", part1(numbers))
	fmt.Println("part2", part2(numbers))
}
