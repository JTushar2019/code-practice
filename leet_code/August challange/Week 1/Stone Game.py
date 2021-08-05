# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3870/
import operator


class Solution:
    def stoneGame(self, piles) -> bool:
        # arr = [0, 0]
        # flag = False
        #
        # def utility(chance, i, j):
        #     nonlocal flag, piles, arr
        #     if i > j:
        #         if arr[0] > arr[1]:
        #             flag = True
        #         return
        #
        #     arr[chance] += piles[i]
        #
        #     utility((chance + 1) % 2, i + 1, j)
        #
        #     if flag:
        #         return
        #
        #     arr[chance] -= piles[i]
        #     arr[chance] += piles[j]
        #
        #     utility((chance + 1) % 2, i, j - 1)
        #
        #     arr[chance] -= piles[j]
        #
        # utility(0, 0, len(piles) - 1)
        # return flag

        return True

# as logic says, anybody can get any pile of stone. cause there is not any greedy approch to win.
# so one has to just play by luck. and by doing that, one can see that any perticular pile can be given
# to either player by a more than one sequnce of distibution.
# so as total piles is odd
# so equal partition cant be done.. hence one is bound to have greater share than the other
# so winning is always possible.
