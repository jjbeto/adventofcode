package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
	"sort"
	"strings"
)

var (
	lines         []string
	autocompletes []string
)

func part1() int {
	var sum int
	tokens := make(map[string]int)
	for _, line := range lines {
		var stack aoc.Stack
		var match int
		var corrupted bool
	LineLoop:
		for _, char := range line {
			curr := string(char)
			if strings.Index("{([<", curr) != -1 {
				stack.Push(curr)
				match++
				continue
			}

			last := stack.Pop()

			switch last + curr {
			case "{}", "()", "[]", "<>":
				match--
			default:
				tokens[curr]++
				corrupted = true
				break LineLoop
			}
		}

		if !corrupted && match != 0 {
			var completion string
			for {
				last := stack.Pop()
				if last == "" {
					break
				}
				switch last {
				case "(":
					completion += ")"
				case "[":
					completion += "]"
				case "{":
					completion += "}"
				case "<":
					completion += ">"
				default:
					panic("not expected: " + last)
				}
			}
			autocompletes = append(autocompletes, completion)
		}
	}
	for char, multiple := range tokens {
		switch char {
		case ")":
			sum += multiple * 3
		case "]":
			sum += multiple * 57
		case "}":
			sum += multiple * 1197
		case ">":
			sum += multiple * 25137
		}
	}
	return sum
}

func part2() int {
	var scores aoc.SortableArray[int]
	for i, each := range autocompletes {
		scores = append(scores, 0)
		for _, char := range each {
			scores[i] = scores[i]*5 + strings.Index(")]}>", string(char)) + 1
		}
	}
	sort.Sort(scores)
	return scores[len(scores)/2]
}

func main() {
	lines = aoc.ReadLines("2021/day10", "data.txt", aoc.ToString)

	fmt.Println("part1", part1())
	fmt.Println("part2", part2())
}
