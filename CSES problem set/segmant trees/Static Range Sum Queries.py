# https://cses.fi/problemset/task/1646/

# import sys
#
# file1 = open("input.txt", "r")
# file2 = open("output.txt", "w")
# sys.stdin = file1
# sys.stdout = file2

size, queries = (int(i) for i in input().split())

array = [int(i) for i in input().split()]

from itertools import accumulate as acc

prefixsum = list(acc([0] + array))

for _ in range(queries):
    low, high = (int(i) for i in input().split())
    print(prefixsum[high] - prefixsum[low - 1])

# file2.close()
# file1.close()