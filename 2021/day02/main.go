package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/helper"
	"strconv"
	"strings"
)

func part1(lines *[]string) int {
	var horizontal, depth int
	for _, line := range *lines {
		split := strings.Fields(line)
		move, err := strconv.Atoi(split[1])
		if err != nil {
			panic(err)
		}
		switch split[0] {
		case "up":
			depth -= move
		case "down":
			depth += move
		case "forward":
			horizontal += move
		}
	}
	return horizontal * depth
}

func part2(lines *[]string) int {
	var horizontal, depth, aim int
	for _, line := range *lines {
		split := strings.Fields(line)
		move, err := strconv.Atoi(split[1])
		if err != nil {
			panic(err)
		}
		switch split[0] {
		case "up":
			aim -= move
		case "down":
			aim += move
		case "forward":
			horizontal += move
			depth += aim * move
		}
	}
	return horizontal * depth
}

func main() {
	lines := helper.ReadLines("2021/day02", "data.txt")
	fmt.Println("part1", part1(&lines))
	fmt.Println("part2", part2(&lines))
}
