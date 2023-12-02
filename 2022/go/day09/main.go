package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
	"strings"
)

var (
	lines []string
)

type coord struct {
	x int
	y int
}

type algo struct {
	size int
	head coord
	tail []coord
	log  map[coord]int
}

func (c *algo) run() int {
	c.head, c.tail, c.log = coord{}, make([]coord, c.size), make(map[coord]int)

	for i := 0; i < c.size; i++ {
		c.tail = append(c.tail, coord{})
	}
	c.log[c.head]++

	for _, line := range lines {
		split := strings.Split(line, " ")
		c.move(split[0], aoc.ToIntBase10(split[1]))
	}
	return len(c.log)
}

func (c *algo) move(direction string, qtd int) {
	for i := 0; i < qtd; i++ {
		switch direction {
		case "R":
			c.head.x++
		case "L":
			c.head.x--
		case "U":
			c.head.y++
		case "D":
			c.head.y--
		}

		head := c.head
		tail := c.tail[0]
		for j := 0; j < c.size; j++ {
			diff := coord{x: head.x - tail.x, y: head.y - tail.y}
			if aoc.Abs(diff.x) <= 1 && aoc.Abs(diff.y) <= 1 {
				break // neighbor
			}
			tail.x += aoc.Sign(diff.x)
			tail.y += aoc.Sign(diff.y)

			c.tail[j] = tail
			head = tail
			tail = c.tail[j+1]
		}

		c.log[c.tail[c.size-1]]++
	}
}

func part1() int {
	algo := algo{size: 1}
	return algo.run()
}

func part2() int {
	algo := algo{size: 9, log: make(map[coord]int)}
	return algo.run()
}

func main() {
	lines = aoc.ReadLines("2022/day09", "data.txt", aoc.ToString)
	fmt.Println("part1", part1())
	fmt.Println("part2", part2())
}
