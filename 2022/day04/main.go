package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
	"strings"
)

func convert(value string) (int, int) {
	split := strings.Split(value, "-")
	return aoc.ToIntBase10(split[0]), aoc.ToIntBase10(split[1])
}

func inRange(x, y, elem int) bool {
	return elem >= x && elem <= y
}

func part1(lines []string) int {
	var total int
	for _, line := range lines {
		split := strings.Split(line, ",")
		x1, y1 := convert(split[0])
		x2, y2 := convert(split[1])
		if (inRange(x1, y1, x2) && inRange(x1, y1, y2)) || (inRange(x2, y2, x1) && inRange(x2, y2, y1)) {
			total++
		}
	}
	return total
}

func part2(lines []string) int {
	var total int
	for _, line := range lines {
		split := strings.Split(line, ",")
		x1, y1 := convert(split[0])
		x2, y2 := convert(split[1])
		if inRange(x1, y1, x2) || inRange(x1, y1, y2) || inRange(x2, y2, x1) || inRange(x2, y2, y1) {
			total++
		}
	}
	return total
}

func main() {
	numbers := aoc.ReadLines("2022/day04", "data.txt", aoc.ToString)
	fmt.Println("part1", part1(numbers))
	fmt.Println("part2", part2(numbers))
}
