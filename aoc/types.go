package aoc

type (
	Signed interface {
		~int | ~int8 | ~int16 | ~int32 | ~int64
	}
	Unsigned interface {
		~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~uintptr
	}
	Integer interface {
		Signed | Unsigned
	}
	Float interface {
		~float32 | ~float64
	}
	Number interface {
		Integer | Float
	}
	Comparable interface {
		Integer | Float | ~string
	}
)

// SortableArray helper struct to allow ease-use of sort.Sort()
type SortableArray[T Comparable] []T

func (array SortableArray[T]) Len() int           { return len(array) }
func (array SortableArray[T]) Swap(i, j int)      { array[i], array[j] = array[j], array[i] }
func (array SortableArray[T]) Less(i, j int) bool { return array[i] < array[j] }
