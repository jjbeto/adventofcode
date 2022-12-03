package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
	"strings"
)

func part1(line string, days int) int {
	population := []int{0, 0, 0, 0, 0, 0, 0, 0, 0}
	for _, each := range strings.Split(line, ",") {
		population[aoc.ToIntBase10(each)]++
	}

	for day := 1; day <= days; day++ {
		population0 := population[0]
		for i := range population[:8] {
			population[i] = population[i+1]
		}
		population[6] += population0
		population[8] = population0
	}

	var sum int
	for _, subtotal := range population {
		sum += subtotal
	}
	return sum
}

func main() {
	line := aoc.ReadLines("2021/day06", "data.txt", aoc.ToString)[0]

	fmt.Println("part1", part1(line, 80))
	fmt.Println("part2", part1(line, 256))
}
