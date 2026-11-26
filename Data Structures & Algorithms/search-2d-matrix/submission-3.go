func searchMatrix(matrix [][]int, target int) bool {
	m, n := len(matrix), len(matrix[0])
	left, right := 0,  m * n - 1
	for left <= right{
		mid := int((left + right) / 2)
		my := mid%n
		mx := mid/n
		mid_value := matrix[mx][my]
		if mid_value == target{
			return true
		}else if mid_value > target{
			right = mid - 1
		}else{
			left = mid + 1
		}
	}
	return false
}
