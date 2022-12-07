package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
	"sort"
	"strings"
)

func calculateSummary(lines []string) map[string]int {
	summary := make(map[string]int)
	var stack aoc.Stack
	for i := 0; i < len(lines); i++ {
		if strings.HasPrefix(lines[i], "$ cd ..") {
			stack.Pop()
			continue
		}
		if strings.HasPrefix(lines[i], "$ cd ") {
			curr := lines[i][5:]
			if stack.IsEmpty() {
				stack.Push(curr)
			} else {
				stack.Push(strings.Join(stack, ".") + "." + lines[i][5:])
			}
			continue
		}

		if lines[i] == "$ ls" {
			for {
				if i == len(lines)-1 || strings.HasPrefix(lines[i+1], "$") {
					break // if is EOF or output has finished, end ls loop
				}
				i++
				if strings.HasPrefix(lines[i], "dir ") {
					continue
				}
				split := strings.Split(lines[i], " ")
				fileSize := aoc.ToIntBase10(split[0])
				for _, dir := range stack {
					summary[dir] += fileSize
				}
			}
		}
	}
	return summary
}

func part1(lines []string) int {
	var result int
	for _, size := range calculateSummary(lines) {
		if size <= 100_000 {
			result += size
		}
	}
	return result
}

func part2(lines []string) int {
	var sum int
	summary := calculateSummary(lines)
	for _, size := range summary {
		sum += size
	}

	spaceNeeded := 30_000_000 - (70_000_000 - summary["/"])
	var shortList aoc.SortableArray[int]
	for _, size := range summary {
		if size >= spaceNeeded {
			shortList = append(shortList, size)
		}
	}
	sort.Sort(shortList)
	return shortList[0]
}

func main() {
	lines := aoc.ReadLines("2022/day07", "data.txt", aoc.ToString)
	fmt.Println("part1", part1(lines))
	fmt.Println("part2", part2(lines))
}
