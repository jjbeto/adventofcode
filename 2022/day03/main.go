package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
	"strings"
)

// translate converts a base ref char code to challenge priority:
// - Lowercase item types a through z have priorities 1 through 26.
// - Uppercase item types A through Z have priorities 27 through 52.
// - char ref: a->97 z->122 A->65 Z->90
func translate(char int32) int32 {
	if char > 96 { // lowercase
		return char - 96 // a=97 -> a=1
	}
	// or uppercase..
	return char - 38 // A=65 -> A=27
}

func part1(lines []string) int32 {
	var sum int32
	for _, line := range lines {
		p1, p2 := line[:len(line)/2], line[len(line)/2:]
		for _, char := range p1 {
			if strings.Index(p2, string(char)) > -1 {
				sum += translate(char)
				break
			}
		}
	}
	return sum
}

func part2(lines []string) int32 {
	var sum int32
	for i := 0; i < len(lines); i += 3 {
		elf1, elf2, elf3 := lines[i], lines[i+1], lines[i+2]
		for _, char := range elf1 {
			if strings.Index(elf2, string(char)) > -1 && strings.Index(elf3, string(char)) > -1 {
				sum += translate(char)
				break
			}
		}
	}
	return sum
}

func main() {
	numbers := aoc.ReadLines("2022/day03", "data.txt", aoc.ToString)
	fmt.Println("part1", part1(numbers))
	fmt.Println("part2", part2(numbers))
}
