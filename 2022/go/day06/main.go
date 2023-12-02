package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
	"strings"
)

func slide(line string, window int) int {
	for i := 0; i <= len(line)-(window-1); i++ {
		block := line[i : i+window]
		found := true
		for _, char := range block {
			if strings.Count(block, string(char)) > 1 {
				found = false
				break
			}
		}
		if found {
			return i + window
		}
	}
	return -1
}

func part1(line string) int {
	return slide(line, 4)
}

func part2(line string) int {
	return slide(line, 14)
}

func main() {
	line := aoc.ReadLines("2022/day06", "data.txt", aoc.ToString)[0]
	fmt.Println("part1", part1(line))
	fmt.Println("part2", part2(line))
}
