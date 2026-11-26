func findMin(nums []int) int {
	n := len(nums) - 1
	left, right := 0, n-1
	for left <= right{
		mid := left + (right-left) / 2
		mid_value := nums[mid]
		if mid_value < nums[n]{
			right = mid - 1
		}else{
			left = mid + 1
		}
	}
	return nums[left]
}
