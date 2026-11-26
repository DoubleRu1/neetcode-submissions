func twoSum(nums []int, target int) []int {
    num_dict := make(map[int]int)
	for idx, num := range nums{
		if target_idx, ok := num_dict[target-num]; ok{
			return []int{target_idx,idx}
		}
		num_dict[num] = idx
	}
	return nil
}
