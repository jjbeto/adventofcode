package aoc

func DFS(lines []string, target string, root Coordinate, visited []Coordinate) []Coordinate {
	if lines[root.X][root.Y:root.Y+1] == target || ContainsCoordinate(visited, root) {
		return visited
	}

	visited = append(visited, root)
	for _, next := range root.Adjacent(len(lines), len(lines[0])) {
		visited = DFS(lines, target, next, visited)
	}
	return visited
}
