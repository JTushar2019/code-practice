# https://leetcode.com/problems/water-and-jug-problem/

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:

        if jug2Capacity < jug1Capacity:
            b1 = jug2Capacity
            b2 = jug1Capacity
        elif jug1Capacity < jug2Capacity:
            b1 = jug1Capacity
            b2 = jug2Capacity
        else:
            b1 = b2 = jug2Capacity

        t = targetCapacity
        if t > b1 + b2 or (t >= b2 and t % b2 > b1):
            return False

        if t == b1 or t == b2:
            return True

        if t > b2:
            t = t % b2
        else:
            t = t % b1

        s = set()
        remaining_water = 0
        while True:
            remaining_water = b1 - ((b2 - remaining_water) % b1)
            if remaining_water == t:
                return True
            if remaining_water in s:
                return False
            else:
                s.add(remaining_water)


s = Solution()
print(s.canMeasureWater(1, 2, 3))
print(s.canMeasureWater(5, 33, 1))
print(s.canMeasureWater(3, 5, 4))
print(s.canMeasureWater(23,46,23))