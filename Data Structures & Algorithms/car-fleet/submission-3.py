class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #sort cars into positions of decreasing order, because cannot overtake
        hashtable = {}
        fleets = 0
        slowest = 0 #time of the fleet directly ahead

        for i in range(len(position)):
            hashtable[position[i]] = speed[i]
        position.sort()

        while position:
            curr = position.pop()
            time = (target - curr) / hashtable[curr]
            if time > slowest:
                slowest = time 
                fleets += 1
            
        return fleets