# https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1/

S = "aabacbebebe"
S = "ssss"
K = 3


def longestKSubstr(s, k):
    from collections import defaultdict
    d = defaultdict(int)
    ans = -2
    i = 0
    j = 0
    count = 0
    while j < len(s):

        if s[j] not in d:
            count += 1
        d[s[j]] += 1


        if count == k:
            ans = max(ans, j - i + 1)

        while count > k:
            if d[s[i]] > 1:
                d[s[i]] -= 1
                i += 1
            else:
                d.pop(s[i])
                count -= 1
                i += 1
                break

        j += 1

    return max(ans, -1)


print(longestKSubstr(S, K))