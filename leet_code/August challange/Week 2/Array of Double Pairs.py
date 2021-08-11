# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3877/

class Solution:
    def canReorderDoubled(self, arr):
        l = len(arr)
        from collections import Counter
        negative = Counter()
        postive = Counter()
        for each in arr:
            if each >= 0:
                postive[each] += 1
            else:
                negative[each] += 1

        for each in sorted(postive.elements()):
            if not postive:
                break
            if each in postive:
                postive[each] -= 1
                if postive[each] == 0:
                    postive.pop(each)
                if each * 2 in postive:
                    postive[each * 2] -= 1
                    if postive[each * 2] == 0:
                        postive.pop(each * 2)
                else:
                    print(False)
                    return False
        for each in sorted(negative.elements())[::-1]:
            if not negative:
                break
            if each in negative:
                negative[each] -= 1
                if negative[each] == 0:
                    negative.pop(each)
                if each * 2 in negative:
                    negative[each * 2] -= 1
                    if negative[each * 2] == 0:
                        negative.pop(each * 2)
                else:
                    print(False)
                    return False
        print(True)
        return True


s = Solution()
s.canReorderDoubled([3, 1, 3, 6])
s.canReorderDoubled([2, 1, 2, 6])
s.canReorderDoubled([4, -2, 2, -4])
s.canReorderDoubled([2, 1, 2, 1, 1, 1, 2, 2])
s.canReorderDoubled([0, 0])
