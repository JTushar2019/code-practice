# https://leetcode.com/problems/the-skyline-problem/

class Solution:
    def getSkyline(self, buildings):
        import heapq as hp
        breaks = []
        for each in buildings:
            breaks.extend([each[0], each[1]])
        hp.heapify(breaks)  # to go over x axis in increasing order.

        heap = []  # to see the greatest height at any stop also with the ending of that building(height, y)
        result = []
        p = 0
        l = len(buildings)
        while breaks:
            curnt_pos = hp.heappop(breaks)
            maxh = 0

            while heap and heap[0][1] <= curnt_pos:  # remove buildings ending at this position or before
                hp.heappop(heap)

            if heap:  # update the max height from building which wont end at this position
                maxh = -heap[0][0]

            while p < l and buildings[p][0] == curnt_pos:  # add to heap and update max for building starting here
                height = buildings[p][2]
                hp.heappush(heap, (-height, buildings[p][1]))  # (height,building_ending)
                maxh = max(maxh, height)
                p += 1

            if result and result[-1][1] == maxh:  # if the last seen height is same then move on
                continue
            else:
                result.append([curnt_pos, maxh])
        print(result)
        return result


s = Solution()
s.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
s.getSkyline([[0, 2, 3], [2, 5, 3]])