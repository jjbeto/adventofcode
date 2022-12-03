package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
	"strings"
)

func part1(lines []string) int {
	var total int
	for _, line := range lines {
		rightSide := strings.Split(line, " | ")[1]
		numbers := strings.Split(rightSide, " ")
		for _, n := range numbers {
			switch len(n) {
			case 2, 3, 4, 7:
				total++
			}
		}
	}
	return total
}

func part2(lines []string) int {
	var sum int
	var unknown []string
	known := []string{"", "", "", "", "", "", "", "", "abcdefg", ""}
	for _, line := range lines {
		split := strings.Split(line, " | ")
		for _, x := range strings.Split(split[0], " ") {
			number := aoc.SortString(x)
			switch len(x) {
			case 2:
				known[1] = number
			case 3:
				known[7] = number
			case 4:
				known[4] = number
			default:
				unknown = append(unknown, number)
			}
		}

		for _, x := range unknown {
			if len(x) != 5 {
				continue
			}
			if aoc.IsSubset(strings.Split(known[7], ""), strings.Split(x, "")) {
				known[3] = x
				continue
			}
			var remain int
			for _, char := range x {
				if strings.Index(known[4], string(char)) == -1 {
					remain++
				}
			}
			if remain == 2 {
				known[5] = x
			} else {
				known[2] = x
			}
		}

		for _, x := range unknown {
			if len(x) != 6 {
				continue
			}

			if !aoc.IsSubset(strings.Split(known[7], ""), strings.Split(x, "")) {
				known[6] = x
				continue
			}
			if aoc.IsSubset(strings.Split(known[3], ""), strings.Split(x, "")) {
				known[9] = x
				continue
			}
			known[0] = x
		}

		var value string
		for _, x := range strings.Split(split[1], " ") {
			number := aoc.SortString(x)
			value += fmt.Sprintf("%v", aoc.Index(known, number))
		}
		sum += aoc.ToIntBase10(value)
	}

	return sum
}

func main() {
	lines := aoc.ReadLines("2021/day08", "data.txt", aoc.ToString)

	fmt.Println("part1", part1(lines))
	fmt.Println("part2", part2(lines))
}
