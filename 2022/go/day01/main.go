package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
	"sort"
)

func part1(lines []string) int {
	var biggest, curr int
	for _, line := range lines {
		if line == "" {
			curr = 0
			continue
		}

		curr += aoc.ToIntBase10(line)

		if curr > biggest {
			biggest = curr
		}
	}
	return biggest
}

func part2(lines []string) int {
	var curr int
	var elves aoc.SortableArray[int]
	for _, line := range lines {
		if line == "" {
			elves = append(elves, curr)
			curr = 0
			continue
		}

		curr += aoc.ToIntBase10(line)
	}
	elves = append(elves, curr) // append the last

	sort.Sort(elves)
	return elves[len(elves)-1] + elves[len(elves)-2] + elves[len(elves)-3]
}

func main() {
	numbers := aoc.ReadLines("2022/day01", "data.txt", aoc.ToString)
	fmt.Println("part1", part1(numbers))
	fmt.Println("part2", part2(numbers))
}
