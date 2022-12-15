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

type Coordinate struct {
	X int
	Y int
}

func (c *Coordinate) Adjacent(xLimit, yLimit int) (coords []Coordinate) {
	if c.X+1 < xLimit {
		coords = append(coords, Coordinate{X: c.X + 1, Y: c.Y}) // up
	}
	if c.X-1 >= 0 {
		coords = append(coords, Coordinate{X: c.X - 1, Y: c.Y}) // down
	}
	if c.Y+1 < yLimit {
		coords = append(coords, Coordinate{X: c.X, Y: c.Y + 1}) // right
	}
	if c.Y-1 >= 0 {
		coords = append(coords, Coordinate{X: c.X, Y: c.Y - 1}) // left
	}
	return
}

func (c *Coordinate) Equals(other Coordinate) bool {
	return c.X == other.X && c.Y == other.Y
}
