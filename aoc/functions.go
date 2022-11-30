package aoc

func ArrayEq[T Comparable](a, b []T) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

// Max return the max element in the list
func Max[T Number](array []T) T {
	var _max T
	for _, value := range array {
		if value > _max {
			_max = value
		}
	}
	return _max
}

// Sum returns the sum of all elements in the list
func Sum[T Number](array []T) T {
	var sum T
	for _, value := range array {
		sum += value
	}
	return sum
}

func SlidingWindow[T Number](aggregator func([]T) T, numbers []T, window int) []T {
	var sliding []T
	for i := 0; i <= len(numbers)-(window-1); i++ {
		sliding = append(sliding, aggregator(numbers[i:i+window]))
	}
	return sliding
}

// RotateMatrix
// 1 2 3     7 8 9      7 4 1
// 4 5 6 --> 4 5 6  --> 8 5 2
// 7 8 9     1 2 3      9 6 3
func RotateMatrix[T any](matrix [][]T, angle int) [][]T {
	sign := 1
	if angle < 0 {
		sign = -1
	}

	for i := 0; i < angle*sign/90; i++ {
		if sign > 0 {
			// +90, +180 ...
			matrix = TransposeMatrix(ReverseMatrix(matrix))
		} else {
			// -90, -180 ...
			matrix = ReverseMatrix(TransposeMatrix(matrix))
		}
	}
	return matrix
}

// ReverseMatrix
// 1 2 3     7 8 9
// 4 5 6 --> 4 5 6
// 7 8 9     1 2 3
func ReverseMatrix[T any](matrix [][]T) [][]T {
	for i, j := 0, len(matrix)-1; i < j; i, j = i+1, j-1 {
		matrix[i], matrix[j] = matrix[j], matrix[i]
	}
	return matrix
}

// TransposeMatrix
// 1 2 3     1 4 7
// 4 5 6 --> 2 5 8
// 7 8 9     3 6 9
func TransposeMatrix[T any](matrix [][]T) [][]T {
	newMatrix := newTransposedMatrix[T](len(matrix[0]), len(matrix))
	for i := 0; i < len(newMatrix); i++ {
		tmp := newMatrix[i]
		for j := 0; j < len(tmp); j++ {
			tmp[j] = matrix[j][i]
		}
	}
	return newMatrix
}

func newTransposedMatrix[T any](cols, lines int) [][]T {
	tmp := make([]T, cols*lines)
	matrix := make([][]T, cols)
	lo, hi := 0, lines
	for i := range matrix {
		matrix[i] = tmp[lo:hi:hi]
		lo, hi = hi, hi+lines
	}
	return matrix
}