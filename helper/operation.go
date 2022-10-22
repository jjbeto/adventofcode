package helper

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
	Operation[T Number] func([]T) T
)

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

func SlidingWindow[T Number](aggregator Operation[T], numbers []T, window int) []T {
	var sliding []T
	for i := 0; i <= len(numbers)-(window-1); i++ {
		sliding = append(sliding, aggregator(numbers[i:i+window]))
	}
	return sliding
}
