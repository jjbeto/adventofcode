package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
	"sort"
	"strings"
)

var (
	lines            []string
	nColumns, nLines int
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

type coord struct {
	x int
	y int
}

func contains(array []coord, elem coord) bool {
	for _, each := range array {
		if each == elem {
			return true
		}
	}
	return false
}

func (c *coord) isValid() bool {
	xValid := c.x > -1 && c.x < nLines
	yValid := c.y > -1 && c.y < nColumns
	return xValid && yValid
}

func adjacent(root coord) (coords []coord) {
	coords = append(coords,
		coord{x: root.x + 1, y: root.y}, // up
		coord{x: root.x - 1, y: root.y}, // down
		coord{x: root.x, y: root.y - 1}, // left
		coord{x: root.x, y: root.y + 1}, // right
	)
	return
}

func dfs(root coord, visited []coord) []coord {
	if lines[root.x][root.y:root.y+1] == "9" || contains(visited, root) {
		return visited
	}

	visited = append(visited, root)
	for _, next := range adjacent(root) {
		if next.isValid() {
			visited = dfs(next, visited)
		}
	}
	return visited
}

func part2(lowPoints []string) int {
	var numbers aoc.SortableArray[int]
	for _, root := range lowPoints {
		split := strings.Split(root, ",")

		root := coord{x: aoc.ToIntBase10(split[0]), y: aoc.ToIntBase10(split[1])}
		visited := dfs(root, []coord{})
		numbers = append(numbers, len(visited))
	}

	sort.Sort(numbers)
	return numbers[len(numbers)-1] * numbers[len(numbers)-2] * numbers[len(numbers)-3]
}

func main() {
	lines = aoc.ReadLines("2021/day09", "data.txt", aoc.ToString)
	nColumns, nLines = len(lines[0]), len(lines)

	i, lowPoints := part1()
	fmt.Println("part1", i)
	fmt.Println("part2", part2(lowPoints))
}
