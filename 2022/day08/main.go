package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
)

var (
	lines []string
)

func getVisibility(x, y int) (left, right, up, down []int) {
	for i := y - 1; i >= 0; i-- {
		left = append(left, aoc.ToIntBase10(lines[x][i:i+1]))
	}
	for i := y + 1; i < len(lines[x]); i++ {
		right = append(right, aoc.ToIntBase10(lines[x][i:i+1]))
	}
	for i := x - 1; i >= 0; i-- {
		up = append(up, aoc.ToIntBase10(lines[i][y:y+1]))
	}
	for i := x + 1; i < len(lines); i++ {
		down = append(down, aoc.ToIntBase10(lines[i][y:y+1]))
	}
	return
}

func isVisible(array []int, curr int) bool {
	for _, each := range array {
		if each >= curr {
			return false
		}
	}
	return true
}

func part1() int {
	var number int
	for x, row := range lines[1 : len(lines)-1] { // ignore first and last rows
		rowIdx := x + 1
		for y, col := range row[1 : len(row)-1] { // ignore first and last cols
			colIdx := y + 1
			mid := aoc.ToIntBase10(string(col))

			left, right, up, down := getVisibility(rowIdx, colIdx)
			if isVisible(left, mid) || isVisible(right, mid) || isVisible(up, mid) || isVisible(down, mid) {
				number++
				continue
			}
		}
	}
	number += len(lines[0]) * 2 // add 1st+last rows
	number += len(lines)*2 - 4  // add 1st+last cols - 1 common elem for rows
	return number
}

func calculateScore(array []int, mid int) int {
	var score int
	for _, each := range array {
		score++
		if each >= mid {
			break
		}
	}
	return score
}

func part2() int {
	var score int
	for x, row := range lines[1 : len(lines)-1] { // ignore first and last rows
		rowIdx := x + 1
		for y, col := range row[1 : len(row)-1] { // ignore first and last cols
			colIdx := y + 1
			mid := aoc.ToIntBase10(string(col))
			left, right, up, down := getVisibility(rowIdx, colIdx)
			newScore := calculateScore(left, mid) * calculateScore(right, mid) * calculateScore(up, mid) * calculateScore(down, mid)
			if newScore > score {
				score = newScore
			}
		}
	}
	return score
}

func main() {
	lines = aoc.ReadLines("2022/day08", "data.txt", aoc.ToString)
	fmt.Println("part1", part1()) // 1818
	fmt.Println("part2", part2()) // 368368
}
