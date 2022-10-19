package helper

func Sum(array []int64) int64 {
	var result int64
	for _, v := range array {
		result += v
	}
	return result
}
