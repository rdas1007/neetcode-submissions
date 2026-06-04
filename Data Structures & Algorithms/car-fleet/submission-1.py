class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = sorted(zip(position, speed), reverse = True)
        fleets = 0
        curr = 0
        for i in time:
            val = (target - i[0])/i[1]
            if val > curr:
                fleets += 1
                curr = val
        return fleets