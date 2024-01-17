# 部分配列の和が最大となるときの値

# 隣の要素ずつ合計する
# 最大値を返す
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_list = []
        sum_list_2 = []
        for i in range(len(nums)-1):
            sum_list.append(nums[i] + nums[i+1])
        max_sum = max(sum_list)
        print(max_sum)
        for j in range(len(sum_list)-1):
            sum_list_2.append(sum_list[j] + sum_list[j+1] - nums[j+1])
        max_sum_2 = max(sum_list_2)
        print(max_sum_2)
        # give up...

# カダネのアルゴリズム（Kadane's Algorithm）
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # set to the minimum possible integer value
        max_sum = float('-inf')
        current_sum = 0
        
        for num in nums:
            current_sum += num
            
            if current_sum > max_sum:
                max_sum = current_sum
            
            if current_sum < 0:
                current_sum = 0
        
        return max_sum