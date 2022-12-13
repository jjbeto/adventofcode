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

type monkey struct {
	items         aoc.Queue[int]
	itemInspected int
	operator      func(int, int) int
	operandOld    bool
	operand       int
	divisible     int
	targetTrue    int
	targetFalse   int
}

func getMonkeys() []*monkey {
	var monkeys []*monkey
	var curr int
	for _, line := range lines {
		switch {
		case strings.HasPrefix(line, "Monkey "):
			curr = aoc.ToIntBase10(line[strings.Index(line, " ")+1 : len(line)-1])
			if len(monkeys) < curr+1 {
				monkeys = append(monkeys, &monkey{})
			}
		case strings.HasPrefix(line, "  Starting items:"):
			for _, each := range strings.Split(line[18:], ", ") {
				monkeys[curr].items = append(monkeys[curr].items, aoc.ToIntBase10(each))
			}
		case strings.HasPrefix(line, "  Operation: new = old "):
			monkeys[curr].operandOld = line[25:] == "old"
			if !monkeys[curr].operandOld {
				monkeys[curr].operand = aoc.ToIntBase10(line[25:])
			}
			if line[23:24] == "+" {
				monkeys[curr].operator = func(x, y int) int { return x + y }
			} else {
				monkeys[curr].operator = func(x, y int) int { return x * y }
			}
		case strings.HasPrefix(line, "  Test: divisible by "):
			monkeys[curr].divisible = aoc.ToIntBase10(line[21:])
		case strings.HasPrefix(line, "    If true: throw to monkey "):
			monkeys[curr].targetTrue = aoc.ToIntBase10(line[29:])
		case strings.HasPrefix(line, "    If false: throw to monkey "):
			monkeys[curr].targetFalse = aoc.ToIntBase10(line[30:])
		default:
			continue
		}
	}
	return monkeys
}

func catchMonkeys(monkeys []*monkey, manageWorry func(int) int, rounds int) int {
	for round := 1; round <= rounds; round++ {
		for _, monkey := range monkeys {
			if monkey.items.IsEmpty() {
				continue
			}
			for {
				worry := monkey.items.Pop()
				monkey.itemInspected++

				if monkey.operandOld {
					worry = monkey.operator(worry, worry)
				} else {
					worry = monkey.operator(worry, monkey.operand)
				}

				worry = manageWorry(worry)

				if worry%monkey.divisible == 0 {
					monkeys[monkey.targetTrue].items = append(monkeys[monkey.targetTrue].items, worry)
				} else {
					monkeys[monkey.targetFalse].items = append(monkeys[monkey.targetFalse].items, worry)
				}

				if monkey.items.IsEmpty() {
					break
				}
			}
		}
	}

	var inspects aoc.SortableArray[int]
	for _, monkey := range monkeys {
		inspects = append(inspects, monkey.itemInspected)
	}
	sort.Sort(inspects)

	return inspects[len(inspects)-1] * inspects[len(inspects)-2]
}

func part1() int {
	monkeys := getMonkeys()
	manageWorry := func(val int) int { return val / 3 }
	return catchMonkeys(monkeys, manageWorry, 20)
}

func part2() int {
	monkeys := getMonkeys()
	var mod int = 1
	for _, monkey := range monkeys {
		mod *= monkey.divisible
	}
	manageWorry := func(val int) int { return val % mod }
	return catchMonkeys(monkeys, manageWorry, 10_000)
}

func main() {
	lines = aoc.ReadLines("2022/day11", "data.txt", aoc.ToString)
	fmt.Println("part1", part1())
	fmt.Println("part2", part2())
}
