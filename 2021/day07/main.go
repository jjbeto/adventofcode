package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
	"strings"
)

func part1(line string) int {
	var tracks []int
	for _, each := range strings.Split(line, ",") {
		tracks = append(tracks, aoc.ToIntBase10(each))
	}

	mean := aoc.Sum(tracks) / len(tracks)
	var best int
	for {
		var fuel1, fuel2, fuel3 int
		for _, track := range tracks {
			fuel1 += aoc.Abs(track - mean + 1)
			fuel2 += aoc.Abs(track - mean)
			fuel3 += aoc.Abs(track - mean - 1)
		}
		// mean is the best
		if fuel1 > fuel2 && fuel2 < fuel3 {
			best = fuel2
			break
		}
		// below mean is better
		if fuel1 < fuel2 {
			mean--
			continue
		}
		// above mean is better
		if fuel3 < fuel2 {
			mean++
			continue
		}
	}

	return best
}

func part2(line string) int {
	var tracks []int
	for _, each := range strings.Split(line, ",") {
		tracks = append(tracks, aoc.ToIntBase10(each))
	}

	mean := aoc.Sum(tracks) / len(tracks)
	var best int
	for {
		var below, mid, above int
		for _, track := range tracks {
			below += aoc.Summation(aoc.Abs(track - mean + 1))
			mid += aoc.Summation(aoc.Abs(track - mean))
			above += aoc.Summation(aoc.Abs(track - mean - 1))
		}
		if below > mid && mid < above {
			best = mid
			break
		}
		if below < mid {
			mean--
			continue
		}
		if above < mid {
			mean++
			continue
		}
	}

	return best
}

func main() {
	line := aoc.ReadLines("2021/day07", "data.txt", aoc.ToString)[0]

	fmt.Println("part1", part1(line))
	fmt.Println("part2", part2(line))
}
