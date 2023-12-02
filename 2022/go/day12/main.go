package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
	"sort"
)

var (
	lines  []string
	xLimit int
	yLimit int
)

func part1(shortest bool) int {
	var start, end aoc.Coordinate
	heightMap := make(map[aoc.Coordinate]rune)
	for x, row := range lines {
		for y, height := range row {
			if height == 'S' {
				start = aoc.Coordinate{X: x, Y: y}
				height = 'a'
			}
			if height == 'E' {
				end = aoc.Coordinate{X: x, Y: y}
				height = 'z'
			}
			heightMap[aoc.Coordinate{X: x, Y: y}] = height
		}
	}

	toVisit := []aoc.Coordinate{start}
	visited := make(map[aoc.Coordinate]bool)
	distance := map[aoc.Coordinate]int{
		start: 0,
	}
	for {
		if len(toVisit) == 0 {
			break
		}

		curr := toVisit[0]
		visited[curr] = true
		toVisit = toVisit[1:]

		if curr == end {
			break
		}

		for _, next := range curr.Adjacent(xLimit, yLimit) {
			if !visited[next] && heightMap[next]-heightMap[curr] <= 1 {
				if distance[next] == 0 {
					toVisit = append(toVisit, next)
					if shortest && heightMap[next] == 'a' {
						distance[next] = distance[curr]
					} else {
						distance[next] = distance[curr] + 1
					}
				}
			}
		}
		sort.Slice(toVisit, func(a, b int) bool {
			return distance[toVisit[a]] < distance[toVisit[b]]
		})
	}

	return distance[end]
}

func main() {
	lines = aoc.ReadLines("2022/day12", "data.txt", aoc.ToString)
	xLimit, yLimit = len(lines), len(lines[0])

	fmt.Println("part1", part1(false))
	fmt.Println("part2", part1(true))
}
