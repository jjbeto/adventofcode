package aoc

type Stack []string

func (s *Stack) IsEmpty() bool {
	return len(*s) == 0
}

func (s *Stack) Push(elem string) {
	*s = append(*s, elem) // Simply append the new value to the end of the stack
}

// Pop remove and return top element of stack. Return false if stack is empty.
func (s *Stack) Pop() string {
	if s.IsEmpty() {
		return ""
	} else {
		i := len(*s) - 1
		elem := (*s)[i]
		*s = (*s)[:i]
		return elem
	}
}
