# [0,1,2,4,5,6,7] の配列が [4,5,6,7,0,1,2] といったように、
# 昇順にソートされた配列が任意のpivotで回転されている
# targetが与えられるため、配列に存在した場合はindexを返し、そうでない場合は-1を返す

# 配列の特性を活かした
class Solution01:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            # midより左側がソートされているか
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    # 右のポインタを更新
                    right = mid - 1
                else:
                    # 左のポインタを更新
                    left = mid + 1
            
            # midより右側がソートされているか
            if nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

# simple solution
class Solution02:
    def search(self, nums: List[int], target: int) -> int:
        if nums.count(target):
            return nums.index(target)
        else:
            return -1
