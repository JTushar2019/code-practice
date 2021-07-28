# Week 1: Programming Assignment 1
# Due on 2021-08-12, 23:59 IST
# Swayam wants to play a game with you. He has an integer with him, S, but he has hid it from you. Instead, he has shared some information about S.
# In particular, for every i such that 1 ≤ i ≤ N, he has told you the value ⌊(i*S)/K⌋. This is given to you as the array A1, A2, ..., AN, where Ai = ⌊(i*S)/K⌋. He has also told you the value of K. But since he has not shared the value of S, you want to find the largest possible range [L,R] in which S could lie. That is, find the largest possible range [L,R] such that, for any integer P ∈ [L,R], Ai is equal to ⌊(i*P)/K⌋ for all i.
# It is guaranteed that such a range always exists and is unique. You may read the sample test cases for more clarity.
#
# Note that ⌊x⌋ denotes floor(x), which is largest integer which is ≤ x.
#
# Input
# The first line of the input contains a single integer T denoting the number of test cases.
# The first line of each test case contains two space-separated integers N and K respectively.
# The second line of each test case contains N space separated integers, A1, A2, ..., AN.
# Output
# For each testcase, print a single line containing two space separated integers L and R respectively.
# Constraints
# 1 ≤ T ≤ 103
# 1 ≤ N ≤ 105
# 1 ≤ K ≤ 109
# 0 ≤ Ai ≤ 1.1*1017, for all possible values of i.
# It is guaranteed that Ai*K doesn't exceed 1.1*1017
# It is guaranteed that 0 ≤ S ≤ 1.1*1012
# Sum of N over all test cases doesn't exceed 5*105
# Example Input
# 4
# 5 10
# 2 4 6 9 11
# 5 100
# 0 0 0 0 1
# 3 1
# 111111111111 222222222222 333333333333
# 2 100
# 10000000000 20000000000
# Example Output
# 23 23
# 20 24
# 111111111111 111111111111
# 1000000000000 1000000000049
# Explanation
# Example case 1:
# Only keeping S=23 satisfies Ai = ⌊(i*S)/K⌋.
# S=23 makes i*S = (23, 46, 69, 92 , 115) which makes ⌊(i*S)/K⌋ = (2 , 4 , 6 , 9 , 11).
# S=22 is not correct answer as its makes i*S = (22, 44, 66, 88, 110), which would make ⌊(i*S)/K⌋ = (2 , 4 , 6 , 8 , 11) which doesn't match with given array A.
#
# Example case 2:
# Only keeping S=20, S=21, S=22, S=23, and S=24 satisfies given array A.
import math

a = [111111111111, 222222222222, 333333333333]
a =[10000000000, 20000000000]
a = [2, 4, 6, 9, 11]
k = 10
n = len(a)
print(math.floor(sum(a) * 2 * k / (n ** 2 + n)))
print((sum(a)-n) * 2 * k / (n ** 2 + n))
for i in range(len(a)):
    a[i] = a[i] * k / (i + 1)

print(a)