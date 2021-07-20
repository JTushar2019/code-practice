# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3330/

# arr = [3,1,3,2,6]
# arr = [1, -2, 3, -2]
# arr = [5,-3,5]
# arr= [0,5,0,8,0,-9,0,9,0,-7,0,3,0,-2]


arr = [52, 183, 124, 154, -170, -191, -240, 107, -178, 171, 75, 186, -125, 61, -298, 284, 21, -73, -294, 253, 146, 248,
       -248, 127, 26, 289, 118, -22, -300, 26, -116, -113, -44, 29, 252, -278, 47, 254, -106, 246, -275, 42, 257, 15,
       96, -298, -69, -104, -239, -95, -4, 76, -202, 156, -14, -178, 188, -84, 78, -195, -125, 28, 109, 125, -25, -53,
       58, 287, 55, -296, 198, 281, 53, -160, 146, 298, 25, -41, -3, 27, -242, 169, 287, -281, 19, 91, 213, 115, 211,
       -218, 124, -25, -272, 278, 296, -177, -166, -192, 97, -49, -25, 168, -81, 6, -94, 267, 293, 146, -1, -258, 256,
       283, -156, 197, 28, 78, 267, -151, -230, -66, 100, -94, -66, -123, 121, -214, -182, 187, 65, -186, 215, 273, 243,
       -99, -76, 178, 59, 190, 279, 300, 217, 67, -117, 170, 163, 153, -37, -147, -251, 296, -176, 117, 68, 258, -159,
       -300, -36, -91, -60, 195, -293, -116, 208, 175, -100, -97, 188, 79, -270, 80, 100, 211, 112, 264, -217, -142, 5,
       105, 171, -264, -247, 138, 275, 227, -86, 30, -219, 153, 10, -66, 267, 22, -56, -70, -234, -66, 89, 182, 110,
       -146, 162, -48, -201, -240, -225, -15, -275, 129, -117, 28, 150, 84, -264, 249, -85, 70, -140, -259, 26, 162, 5,
       -203, 143, 184, 101, 140, 207, 131, 177, 274, -178, -79, 14, -36, 104, 52, 31, 257, 273, -52, 74, 276, 104, -133,
       -255, 188, -252, 229, 200, -74, -39, -250, 142, -201, -196, -43, -40, 255, -149, -299, -197, -175, -96, -155,
       -196, -24, 12, 79, 71, -144, -59, -120, 227, -256, -163, -297, 116, 286, -283, -31, -221, -41, 121, -170, 160,
       205, 8, 88, 25, -272, -107, 292, -180, 299, 94, -97, -81, -134, 37, 238]


def maxSubarraySumCircular(nums):
    from itertools import accumulate as acc
    import operator
    left = [nums[0]]*len(nums)
    ans = nums[0]
    for i in range(1, len(nums)):
        left[i] = max(left[i-1] + nums[i], nums[i])
        ans = max(ans, left[i])

    leftmost = acc(nums, operator.add)
    leftmost = list(acc(leftmost, max))

    rightmost = acc(nums[::-1], operator.add)
    rightmost = acc(rightmost, max)
    rightmost = list(rightmost)[::-1]

    for i in range(len(nums) - 1):
        ans = max(ans, leftmost[i] + rightmost[i + 1])

    return ans


print(maxSubarraySumCircular(arr))