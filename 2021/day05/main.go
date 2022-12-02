package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
	"strings"
)

func point(x, y int) string {
	return fmt.Sprintf("%v,%v", x, y)
}

func execute(lines []string, diagonals bool) int {
	points := make(map[string]int)
	for _, line := range lines {
		split := strings.Split(line, " -> ")

		from := strings.Split(split[0], ",")
		x1 := aoc.ToIntBase10(from[0])
		y1 := aoc.ToIntBase10(from[1])

		to := strings.Split(split[1], ",")
		x2 := aoc.ToIntBase10(to[0])
		y2 := aoc.ToIntBase10(to[1])

		if !diagonals && x1 != x2 && y1 != y2 {
			continue
		}

		for x1 != x2 || y1 != y2 {
			points[point(x1, y1)]++
			switch {
			case x1 > x2:
				x1--
			case x1 < x2:
				x1++
			}
			switch {
			case y1 > y2:
				y1--
			case y1 < y2:
				y1++
			}
		}
		points[point(x2, y2)]++
	}

	var count int
	for _, val := range points {
		if val > 1 {
			count++
		}
	}

	return count
}

func part1(lines []string) int {
	return execute(lines, false)
}

func part2(lines []string) int {
	return execute(lines, true)
}

func main() {
	lines := aoc.ReadLines("2021/day05", "data.txt", aoc.ToString)

	fmt.Println("part1", part1(lines))
	fmt.Println("part2", part2(lines))
}
