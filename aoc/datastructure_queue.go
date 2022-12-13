package aoc

type Queue[T any] []T

func (s *Queue[T]) IsEmpty() bool {
	return len(*s) == 0
}

func (s *Queue[T]) Push(elem T) {
	*s = append(*s, elem)
}

func (s *Queue[T]) Pop() T {
	if s.IsEmpty() {
		var empty T
		return empty
	} else {
		elem := (*s)[0]
		*s = (*s)[1:]
		return elem
	}
}
