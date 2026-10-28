class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_arr = []
        suffix_arr = []
        area = 0
        #min(prefix[i], suffix[i]) - height[i]
        i = 0
        for i in range(len(height)):
            j = len(height) - i - 1
            if prefix_arr:
                prefix_arr.append(max(height[i], prefix_arr[-1]))
            else:
                prefix_arr.append(height[i])
            if suffix_arr:
                suffix_arr.append(max(height[j], suffix_arr[-1]))
            else:
                suffix_arr.append(height[j])
        for i in range(len(height)):
            area += min(prefix[i], suffix[len(height) - i - 1]) - height[i]
        return area