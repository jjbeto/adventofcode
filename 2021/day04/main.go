package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
	"strings"
)

type board struct {
	matches map[string]int
	numbers map[int]int
}

func (b *board) addMatch(match string) {
	b.matches[match] = 0
}

func (b *board) addNumber(number int) {
	b.numbers[number] = 0
}

func (b *board) drawnNumber(number int) bool {
	b.numbers[number]++
	for each := range b.matches {
		if strings.Index(each, fmt.Sprintf("[%v]", number)) > -1 {
			b.matches[each]++
			if b.matches[each] == 5 {
				return true
			}
		}
	}
	return false
}

func (b *board) getSum() (sum int) {
	for number, val := range b.numbers {
		if val == 0 {
			sum += number
		}
	}
	return
}

func loadGame(lines []string) (boards []board, numbers []int) {
	var cols []string
	boardIndex := -1
	for _, line := range lines[1:] {
		if line == "" {
			if len(cols) > 0 {
				for _, col := range cols {
					boards[boardIndex].addMatch(col)
				}
			}

			cols = []string{}
			boardIndex++
			boards = append(boards, board{matches: make(map[string]int), numbers: make(map[int]int)})
			continue
		}

		row := ""
		var colIdx int
		for _, each := range strings.Split(line, " ") {
			if each == "" {
				continue
			}
			boards[boardIndex].addNumber(aoc.ToIntBase10(each))

			row += "[" + each + "]"

			if len(cols) == colIdx {
				cols = append(cols, "")
			}
			cols[colIdx] += "[" + each + "]"
			colIdx++
		}
		boards[boardIndex].addMatch(row)
	}
	// add last cols
	for _, col := range cols {
		boards[boardIndex].addMatch(col)
	}

	for _, i := range strings.Split(lines[0], ",") {
		number := aoc.ToIntBase10(i)
		numbers = append(numbers, number)
	}

	return
}

func part1(lines []string) int {
	boards, numbers := loadGame(lines)
	var winner board
	var lastNumber int
AllLoops:
	for _, number := range numbers {
		for _, b := range boards {
			if b.drawnNumber(number) {
				winner = b
				lastNumber = number
				break AllLoops
			}
		}
	}

	return lastNumber * winner.getSum()
}

func part2(lines []string) int {
	boards, numbers := loadGame(lines)
	var winner board
	var lastNumber int
	for _, number := range numbers {
		var i int
		for len(boards) > i {
			b := boards[i]
			if b.drawnNumber(number) {
				boards = append(boards[:i], boards[i+1:]...)
				lastNumber = number
				winner = b
				continue
			}
			i++ // only increment if curr board is not a winner
		}
	}

	return lastNumber * winner.getSum()
}

func main() {
	lines := aoc.ReadLines("2021/day04", "data.txt", aoc.ToString)

	fmt.Println("part1", part1(lines))
	fmt.Println("part2", part2(lines))
}
