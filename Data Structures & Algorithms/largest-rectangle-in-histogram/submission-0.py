class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #Stack with index and smallest height 
        stack = []
        largest_area = 0

        for i in range(len(heights)):
            h = heights[i]
            #compute the left area, when encounter a higher col
            start = i
            while stack and h < stack[-1][0]:
                #Pop and calculate the area
                height, start = stack.pop()
                area = height * (i - start)
                if area > largest_area:
                    largest_area = area

            stack.append((h, start))
        if stack:
            for height, start in stack:
                area = height * (len(heights) - start)
                largest_area = max(largest_area, area)
        return largest_area
            