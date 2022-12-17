package main

import (
	"encoding/json"
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
	"reflect"
	"sort"
)

var (
	lines []string
)

func convert(packet string) []any {
	var array []any
	if err := json.Unmarshal([]byte(packet), &array); err != nil {
		panic(err)
	}
	return array
}

// 1=right order, 0=equals, -1=not right order
func compare(left, right []any) int {
	biggest := len(left)
	if biggest < len(right) {
		biggest = len(right)
	}
	for i := 0; i < biggest; i++ {
		if i >= len(left) {
			return 1
		}
		if i >= len(right) {
			return -1
		}

		leftNum, leftIsNum := left[i].(float64)
		rightNum, rightIsNum := right[i].(float64)

		var inOrder int
		switch {
		case leftIsNum && rightIsNum: // int+int
			if leftNum < rightNum {
				inOrder = 1
			}
			if leftNum > rightNum {
				inOrder = -1
			}
		case !leftIsNum && !rightIsNum: // list+list
			inOrder = compare(left[i].([]any), right[i].([]any))
		case !leftIsNum && rightIsNum: // list+int
			inOrder = compare(left[i].([]any), []any{rightNum})
		case leftIsNum && !rightIsNum: // list+int
			inOrder = compare([]any{leftNum}, right[i].([]any))
		}

		if inOrder != 0 {
			return inOrder
		}
	}

	return 0
}

func part1() int {
	var indices []int
	for i := 0; i < len(lines); i += 3 {
		left := convert(lines[i])
		right := convert(lines[i+1])
		if compare(left, right) > 0 {
			indices = append(indices, i/3+1)
		}
	}

	fmt.Printf("%v\n", indices)
	return aoc.Sum(indices)
}

func part2() int {
	var packets [][]any
	for _, line := range lines {
		if line == "" {
			continue
		}
		packets = append(packets, convert(line))
	}

	divider1 := convert("[[2]]")
	divider2 := convert("[[6]]")
	packets = append(packets, divider1, divider2)

	sort.Slice(packets, func(a, b int) bool {
		return compare(packets[a], packets[b]) > 0
	})

	d1, d2 := -1, -1
	for i, p := range packets {
		if reflect.DeepEqual(p, divider1) {
			d1 = i + 1
		} else if reflect.DeepEqual(p, divider2) {
			d2 = i + 1
			continue
		} else if d1 >= 0 && d2 >= 0 {
			break
		}
	}

	return d1 * d2
}

func main() {
	lines = aoc.ReadLines("2022/day13", "data.txt", aoc.ToString)

	fmt.Println("part1", part1())
	fmt.Println("part2", part2()) // 24477
}
