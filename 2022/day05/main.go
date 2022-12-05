package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
)

func part1(lines []string) int {
	return len(lines)
}

func part2(lines []string) int {
	return len(lines)
}

func main() {
	numbers := aoc.ReadLines("2022/day02", "test.txt", aoc.ToString)
	fmt.Println("part1", part1(numbers))
	fmt.Println("part2", part2(numbers))
}
