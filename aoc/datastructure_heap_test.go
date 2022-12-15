package aoc

import (
	"testing"
)

func Test_Heap(t *testing.T) {
	for _, tt := range []struct {
		usecase       string
		base          []int
		isMax         func(int, int) bool
		inserts       []int
		assertFirst   []int
		assertExtract []int
	}{
		{
			usecase:       "max-heap",
			base:          []int{},
			isMax:         func(a, b int) bool { return a > b },
			inserts:       []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 0},
			assertFirst:   []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 9},
			assertExtract: []int{9, 8, 7, 6, 5, 4, 3, 2, 1, 0},
		},
		{
			usecase:       "min-heap",
			base:          []int{},
			isMax:         func(a, b int) bool { return a < b },
			inserts:       []int{9, 8, 7, 6, 5, 4, 3, 2, 1, 0},
			assertFirst:   []int{9, 8, 7, 6, 5, 4, 3, 2, 1, 0},
			assertExtract: []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9},
		},
	} {
		heap := NewHeap(tt.isMax)

		for i, val := range tt.inserts {
			heap.Insert(val)
			if heap.array[0] != tt.assertFirst[i] {
				t.Fatalf("[%v] expected first element to be %v, got %v\n", tt.usecase, tt.assertFirst[i], heap.array[0])
			}
		}

		for _, val := range tt.assertExtract {
			extracted, err := heap.Extract()
			if err != nil {
				t.Fatalf("[%v] error when extracting: %v", tt.usecase, err)
			}
			if val != extracted {
				t.Fatalf("[%v] expected extracted to be %v, got %v\n", tt.usecase, val, extracted)
			}
		}
	}
}
