// https://adventofcode.com/2021/day/3

package main

import (
	"fmt"
	"github.com/jjbeto/adventofcode/aoc"
	"strings"
)

func part1(lines []string) int64 {
	var gamma, epsilon string
	nCols := len(lines[0])
	nLines := len(lines)

	for x := 0; x < nCols; x++ {
		nOnes := 0
		for y := 0; y < nLines; y++ {
			if lines[y][x:x+1] == "1" {
				nOnes++
			}
		}
		if nOnes > nLines/2 {
			gamma += "1"
			epsilon += "0"
			continue
		}
		gamma += "0"
		epsilon += "1"
	}

	return aoc.ToIntBase2(gamma) * aoc.ToIntBase2(epsilon)
}

func filter(lines []string, prefix string) (filtered []string) {
	for _, val := range lines {
		if strings.HasPrefix(val, prefix) {
			filtered = append(filtered, val)
		}
	}
	return filtered
}

func part2(lines []string) int64 {
	oxygen := lines
	co2 := lines
	var oxygenPrefix, co2Prefix string
	nCols := len(lines[0])

	for x := 0; x < nCols; x++ {
		// check oxygen
		if len(oxygen) > 1 {
			nOnes := 0
			for y := 0; y < len(oxygen); y++ {
				if oxygen[y][x:x+1] == "1" {
					nOnes++
				}
			}
			nZeros := len(oxygen) - nOnes
			if nOnes >= nZeros {
				oxygenPrefix += "1"
			} else {
				oxygenPrefix += "0"
			}
			oxygen = filter(oxygen, oxygenPrefix)
		}

		// check co2
		if len(co2) > 1 {
			nOnes := 0
			for y := 0; y < len(co2); y++ {
				if co2[y][x:x+1] == "1" {
					nOnes++
				}
			}
			nZeros := len(co2) - nOnes
			if nZeros <= nOnes {
				co2Prefix += "0"
			} else {
				co2Prefix += "1"
			}
			co2 = filter(co2, co2Prefix)
		}

		if len(co2) == 1 && len(oxygen) == 1 {
			break
		}
	}

	return aoc.ToIntBase2(oxygen[0]) * aoc.ToIntBase2(co2[0])
}

func main() {
	lines := aoc.ReadLines("2021/day03", "data.txt", aoc.ToString)
	fmt.Println("part1", part1(lines))
	fmt.Println("part2", part2(lines))
}
