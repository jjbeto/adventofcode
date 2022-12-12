package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
	"strings"
)

var (
	lines []string
)

func part1() int {
	var cycles, signalStrength int
	x := 1
	for _, line := range lines {
		split := strings.Split(line, " ")
		cycle := 1
		value := 0
		if split[0] == "addx" {
			cycle++
			value = aoc.ToIntBase10(split[1])
		}
		for i := 0; i < cycle; i++ {
			cycles++
			if cycles == 20 || (cycles-20)%40 == 0 {
				signalStrength += cycles * x
			}
		}
		x += value
	}
	return signalStrength
}

func part2() {
	var screen string
	var cycles, lineNumber, x int
	x++
	for _, line := range lines {
		split := strings.Split(line, " ")
		cycle, value := 1, 0
		if split[0] == "addx" {
			cycle++
			value = aoc.ToIntBase10(split[1])
		}
		for i := 0; i < cycle; i++ {
			if len(screen)%40 == 0 && cycles > 0 {
				lineNumber++
			}
			switch x + lineNumber*40 {
			case cycles - 1, cycles, cycles + 1:
				screen += "#"
			default:
				screen += "."
			}
			cycles++
		}
		x += value
	}
	fmt.Printf("%v\n", screen[0:40])
	fmt.Printf("%v\n", screen[40:80])
	fmt.Printf("%v\n", screen[80:120])
	fmt.Printf("%v\n", screen[120:160])
	fmt.Printf("%v\n", screen[160:200])
	fmt.Printf("%v\n", screen[200:240])
}

func main() {
	lines = aoc.ReadLines("2022/day10", "data.txt", aoc.ToString)
	fmt.Println("part1", part1())
	part2()
}
