from builtins import list


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return [[]]
        result = []
        for i in range(len(nums)):
            permuted_lists = self.permute(nums[:i] + nums[i + 1:])
            for permuted_list in permuted_lists:
                permuted_list.insert(0, nums[i])
                result.append(permuted_list)

        return result