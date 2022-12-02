package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
)

/**
- Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
- shape points: 1 for Rock, 2 for Paper, and 3 for Scissors
- A for Rock, B for Paper, and C for Scissors
- X for Rock, Y for Paper, and Z for Scissors
- play returns 0 if you lost, 3 if the round was a draw, and 6 if you won
*/

func part1(lines []string) int {
	var tournament = make(map[string]int)
	for _, line := range lines {
		tournament[line]++
	}

	points := make(map[string]int)
	// lost
	points["B X"] = 0 + 1 // Paper defeats Rock
	points["C Y"] = 0 + 2 // Scissors defeats Paper
	points["A Z"] = 0 + 3 // Rock defeats Scissors
	// draw
	points["A X"] = 3 + 1 // all Rock
	points["B Y"] = 3 + 2 // all Paper
	points["C Z"] = 3 + 3 // all Scissors
	// win
	points["C X"] = 6 + 1 // Rock defeats Scissors
	points["A Y"] = 6 + 2 // Paper defeats Rock
	points["B Z"] = 6 + 3 // Scissors defeats Paper

	var sum int
	for match, total := range tournament {
		sum += points[match] * total
	}
	return sum
}

func part2(lines []string) int {
	var tournament = make(map[string]int)
	for _, line := range lines {
		tournament[line]++
	}

	points := make(map[string]int)
	// lost
	points["B X"] = 0 + 1 // Paper defeats Rock
	points["C X"] = 0 + 2 // Scissors defeats Paper
	points["A X"] = 0 + 3 // Rock defeats Scissors
	// draw
	points["A Y"] = 3 + 1 // all Rock
	points["B Y"] = 3 + 2 // all Paper
	points["C Y"] = 3 + 3 // all Scissors
	// win
	points["C Z"] = 6 + 1 // Rock defeats Scissors
	points["A Z"] = 6 + 2 // Paper defeats Rock
	points["B Z"] = 6 + 3 // Scissors defeats Paper

	var sum int
	for match, total := range tournament {
		sum += points[match] * total
	}
	return sum
}

func main() {
	numbers := aoc.ReadLines("2022/day02", "data.txt", aoc.ToString)
	fmt.Println("part1", part1(numbers)) // guessed 8572 (too low)
	fmt.Println("part2", part2(numbers))
}
