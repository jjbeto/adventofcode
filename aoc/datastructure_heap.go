package aoc

import "fmt"

// Heap https://en.wikipedia.org/wiki/Heap_(data_structure)
type Heap[T Comparable] struct {
	array []T
	max   bool
}

func NewHeap[T Comparable](array []T, isMax bool) *Heap[T] {
	return &Heap[T]{array: array, max: isMax}
}

func (h *Heap[T]) Insert(element T) {
	h.array = append(h.array, element)
	h.heapfy(len(h.array) - 1)
}

func (h *Heap[T]) Extract() (T, error) {
	if len(h.array) == 0 {
		var result T
		return result, fmt.Errorf("no more elements found")
	}
	target := h.array[0]
	last := len(h.array) - 1
	h.array[0] = h.array[last]
	h.array = h.array[:last]
	h.heapfy(0)
	return target, nil
}

func (h *Heap[T]) heapfy(current int) {
	if current > 0 { // if current > 0 then heapfy upstream
		for i := 0; i < len(h.array); i++ {
			p := parent(current)
			if h.check(h.array[current], h.array[p]) {
				h.swap(current, p)
				current = p
			}
		}
		return
	}

	last := len(h.array) - 1
	l, r := left(current), right(current)
	var selected int
	for l <= last {
		switch {
		case l == last:
			selected = l
		case h.check(h.array[l], h.array[r]):
			selected = l
		default:
			selected = r
		}

		if h.check(h.array[selected], h.array[current]) {
			h.swap(current, selected)
			current = selected
			l, r = left(current), right(current)
		} else {
			return
		}
	}
}

func (h *Heap[T]) check(current, next T) bool {
	if h.max {
		return current > next
	}
	return current < next
}

func (h *Heap[T]) swap(a, b int) {
	h.array[a], h.array[b] = h.array[b], h.array[a]
}

// left returns the index of left child node
func left(index int) int {
	return index*2 + 1
}

// right returns the index of right child node
func right(index int) int {
	return index*2 + 2
}

// parent returns the index of parent node
func parent(index int) int {
	return (index - 1) / 2 // even is right child / odd is left child
}
