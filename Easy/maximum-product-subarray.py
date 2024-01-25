# 部分配列の積が最大となるときの値

# 0以下の要素数をカウントしていけないか…?
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_product = nums[0]
        largest_product = []
        minus_list = [x for x in nums if x <= 0]
        count = len(minus_list)
        for num in nums:
            if num <= 0:
                if count == 1:
                    largest_product.append(current_product)
                    current_product = 1
                    break
                if count > 1:
                    current_product *= num
                    count -= -1
            else:
                current_product *= num
        result = max(largest_product)
        return result

# the minimum productはnegativeとの掛け算で大きい値になりうるため
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max, current_min = 1, 1
        res = nums[0]

        for n in nums:
            # タプルにnがあるのは部分配列の開始をリセットするため
            vals = (n, n * current_max, n * current_min)
            current_max, current_min = max(vals), min(vals)

            res = max(res, current_max)
        
        return res