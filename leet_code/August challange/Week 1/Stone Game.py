# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3870/


class Solution:
    def stoneGame(self, piles) -> bool:
        arr = [0, 0]
        flag = False
        s = sum(piles)
        t = (s // 2)

        def utility(chance, i, j):
            nonlocal flag, piles, arr, t
            if arr[1] > t:
                return
            if i > j:
                if arr[0] > arr[1]:
                    flag = True
                return

            arr[chance] += piles[i]

            utility((chance + 1) % 2, i + 1, j)

            if flag:
                return

            arr[chance] -= piles[i]
            arr[chance] += piles[j]

            utility((chance + 1) % 2, i, j - 1)

            arr[chance] -= piles[i]

        utility(0, 0, len(piles) - 1)
        return flag
