import "slices"
func threeSum(nums []int) [][]int {
	m := len(nums)
	if m < 3{
		return nil
	}
	slices.Sort(nums)
	ans := [][]int{}
	i:=0
	for i<m-2{
		j, k := i+1, m-1
		for j < k{
			total := nums[i] + nums[j] + nums[k]
			if total==0{
				ans = append(ans, []int{nums[i], nums[j], nums[k]})
				for j < m-1 && nums[j+1] == nums[j]{
					j += 1
				}
				j += 1
			}else if total > 0{
				k -= 1
			}else{
				j += 1
			}
		}
		for i < m-2 && nums[i+1] == nums[i]{
			i += 1
		}
		i+=1
	}
	return ans
}
