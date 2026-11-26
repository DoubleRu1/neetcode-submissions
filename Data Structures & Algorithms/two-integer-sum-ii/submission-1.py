class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        total = 0
        m = len(numbers)
        for i in range(m-1):
            for j in range(i+1,m):
                total = numbers[i] + numbers[j]
                if total == target:
                    return [i+1,j+1]
