func twoSum(nums []int, target int) []int {
    num_dict := make(map[int]int)
	for idx, num := range nums{
		target_idx := num_dict[target-num]
		if target_idx != 0 {
			return []int{target_idx-1, idx}
		}
		num_dict[num] = idx+1
	}
	return nil
}
