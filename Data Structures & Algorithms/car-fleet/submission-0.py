class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #sort cars into positions of decreasing order, because cannot overtake
        hashtable = {}
        hashtable_ans = {}
        fleets = 0
        for i in range(len(position)):
            hashtable[position[i]] = speed[i]
        position.sort()

        while position:
            curr = position.pop()
            time = (target - curr) / hashtable[curr]
            if time not in hashtable_ans:
                hashtable_ans[time] = 0
                fleets += 1
        return fleets