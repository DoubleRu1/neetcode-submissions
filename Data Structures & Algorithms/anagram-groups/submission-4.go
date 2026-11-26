func groupAnagrams(strs []string) [][]string {
	strs_map := make(map[[26]int][]string)

	for _, str := range strs{
		str_array := [26]int{}
		for _, ch := range str{
			str_array[ch-'a'] += 1
		}
		strs_map[str_array] = append(strs_map[str_array],str)
	}
	// fmt.Println(strs_map)
	answer := [][]string{}
	for _, value := range strs_map {
    	// fmt.Println(value)
		answer = append(answer, value)
	}
	return answer
}
