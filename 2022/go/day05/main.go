package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
	"strings"
)

var (
	lines []string
)

func load() (stacks []aoc.Stack, actions [][]int) {
	var sep int
	for i, line := range lines {
		if line == "" {
			sep = i
		}
	}

	for _, char := range lines[sep-1] {
		if string(char) != " " {
			stacks = append(stacks, aoc.Stack{})
		}
	}

	for _, line := range aoc.Reverse(lines[:sep-1]) {
		i := 0
		for pos := 0; pos <= len(line); pos += 4 {
			curr := line[pos : pos+3]
			if curr != "   " && curr != "" {
				stacks[i].Push(curr)
			}
			i++
		}
	}

	for _, line := range lines[sep+1:] {
		split := strings.Split(line, " ")
		cranes := aoc.ToIntBase10(split[1])
		fromStack := aoc.ToIntBase10(split[3])
		toStack := aoc.ToIntBase10(split[5])
		actions = append(actions, []int{cranes, fromStack, toStack})
	}

	return
}

func part1() string {
	stacks, actions := load()
	for _, operation := range actions {
		cranes := operation[0]
		fromStack := operation[1]
		toStack := operation[2]
		for i := 0; i < cranes; i++ {
			stacks[toStack-1].Push(stacks[fromStack-1].Pop())
		}
	}

	var result string
	for _, stack := range stacks {
		pop := stack.Pop()
		result += pop[1 : len(pop)-1]
	}
	return result
}

func part2() string {
	stacks, actions := load()
	for _, operation := range actions {
		cranes := operation[0]
		fromStack := operation[1]
		toStack := operation[2]
		var moves []string
		for i := 0; i < cranes; i++ {
			if !stacks[fromStack-1].IsEmpty() {
				moves = append(moves, stacks[fromStack-1].Pop())
			}
		}
		for _, each := range aoc.Reverse(moves) {
			stacks[toStack-1].Push(each)
		}
	}

	var result string
	for _, stack := range stacks {
		pop := stack.Pop()
		result += pop[1 : len(pop)-1]
	}
	return result
}

func main() {
	lines = aoc.ReadLines("2022/day05", "data.txt", aoc.ToString)

	fmt.Println("part1", part1())
	fmt.Println("part2", part2())
}
