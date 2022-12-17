package aoc

type Stack[T any] []T

func (s *Stack[T]) IsEmpty() bool {
	return len(*s) == 0
}

func (s *Stack[T]) Push(elem T) {
	*s = append(*s, elem) // Simply append the new value to the end of the stack
}

// Pop remove and return top element of stack. Return false if stack is empty.
func (s *Stack[T]) Pop() T {
	if s.IsEmpty() {
		var empty T
		return empty
	} else {
		i := len(*s) - 1
		elem := (*s)[i]
		*s = (*s)[:i]
		return elem
	}
}

func (s *Stack[T]) Peek() T {
	if s.IsEmpty() {
		var empty T
		return empty
	} else {
		i := len(*s) - 1
		elem := (*s)[i]
		return elem
	}
}
