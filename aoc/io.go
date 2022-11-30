package aoc

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
)

type Transform[T any] func(string) T

func ReadLines[T any](folder, filename string, fn Transform[T]) []T {
	_filename, _ := filepath.Abs(fmt.Sprintf("%v/%v", folder, filename))
	file, err := os.Open(_filename)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var lines []T
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, fn(scanner.Text()))
	}
	if scanner.Err() != nil {
		panic(scanner.Err())
	}
	return lines
}
