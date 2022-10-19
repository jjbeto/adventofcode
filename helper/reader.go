package helper

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"strconv"
)

func ReadLines(year, filename string) []string {
	_filename, _ := filepath.Abs(fmt.Sprintf("%v/%v", year, filename))
	file, err := os.Open(_filename)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	if scanner.Err() != nil {
		panic(scanner.Err())
	}
	return lines
}

func ReadNumbers(year, filename string, base int) []int64 {
	textLines := ReadLines(year, filename)
	var lines []int64
	for _, line := range textLines {
		i, err := strconv.ParseInt(line, base, 0)
		if err != nil {
			panic(err)
		}
		lines = append(lines, i)
	}
	return lines
}
