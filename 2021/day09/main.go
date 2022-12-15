package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
	"sort"
	"strings"
)

var (
	lines []string
)

func part1() (total int, lowPoints []string) {
	for rowIdx, row := range lines {
		for colIdx := range row {
			mid := aoc.ToIntBase10(row[colIdx : colIdx+1])
			if mid == 9 {
				continue // skip 9s
			}
			up, down, left, right := 9, 9, 9, 9
			if rowIdx > 0 {
				up = aoc.ToIntBase10(lines[rowIdx-1][colIdx : colIdx+1])
			}
			if rowIdx < len(lines)-1 {
				down = aoc.ToIntBase10(lines[rowIdx+1][colIdx : colIdx+1])
			}
			if colIdx > 0 {
				left = aoc.ToIntBase10(row[colIdx-1 : colIdx])
			}
			if colIdx < len(row)-1 {
				right = aoc.ToIntBase10(row[colIdx+1 : colIdx+2])
			}

			if mid < up && mid < down && mid < left && mid < right {
				total += mid + 1
				lowPoints = append(lowPoints, fmt.Sprintf("%v,%v", rowIdx, colIdx))
			}
		}
	}
	return
}

func part2(lowPoints []string) int {
	var numbers aoc.SortableArray[int]
	for _, root := range lowPoints {
		split := strings.Split(root, ",")

		root := aoc.Coordinate{X: aoc.ToIntBase10(split[0]), Y: aoc.ToIntBase10(split[1])}
		visited := aoc.DFS(lines, "9", root, []aoc.Coordinate{})
		numbers = append(numbers, len(visited))
	}

	sort.Sort(numbers)
	return numbers[len(numbers)-1] * numbers[len(numbers)-2] * numbers[len(numbers)-3]
}

func main() {
	lines = aoc.ReadLines("2021/day09", "data.txt", aoc.ToString)

	i, lowPoints := part1()
	fmt.Println("part1", i)
	fmt.Println("part2", part2(lowPoints))
}
