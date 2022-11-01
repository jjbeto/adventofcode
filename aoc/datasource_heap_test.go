package aoc

import (
	"testing"
)

func Test_Heap(t *testing.T) {
	for _, tt := range []struct {
		usecase       string
		base          []int
		isMax         bool
		inserts       []int
		assertFirst   []int
		assertExtract []int
	}{
		{
			usecase:       "max-heap with initial arr",
			base:          []int{50, 16, 48, 14, 8, 34, 20, 9, 1, 5, 7},
			isMax:         true,
			inserts:       []int{64},
			assertFirst:   []int{64},
			assertExtract: []int{64, 50, 48, 34, 20, 16, 14, 9, 8, 7, 5, 1},
		},
		{
			usecase:       "max-heap",
			base:          []int{},
			isMax:         true,
			inserts:       []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 0},
			assertFirst:   []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 9},
			assertExtract: []int{9, 8, 7, 6, 5, 4, 3, 2, 1, 0},
		},
		{
			usecase:       "min-heap",
			base:          []int{},
			isMax:         false,
			inserts:       []int{9, 8, 7, 6, 5, 4, 3, 2, 1, 0},
			assertFirst:   []int{9, 8, 7, 6, 5, 4, 3, 2, 1, 0},
			assertExtract: []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9},
		},
	} {
		heap := NewHeap(tt.base, tt.isMax)

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
