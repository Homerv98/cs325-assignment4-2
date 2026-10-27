def max_independent_set(nums):
    n = len(nums)

    if n == 0:
        return []

    # dp[i] stores the maximum sum using the first i elements
    dp = [0] * (n + 1)

    dp[1] = max(0, nums[0])

    # Build the DP table
    for i in range(2, n + 1):
        include = nums[i - 1] + dp[i - 2]
        exclude = dp[i - 1]

        dp[i] = max(include, exclude)

    # Reconstruct the chosen subsequence
    result = []
    i = n

    while i >= 1:
        if dp[i] == dp[i - 1]:
            # Current element was not selected
            i -= 1
        else:
            # Current element was selected
            result.append(nums[i - 1])
            i -= 2

    result.reverse()

    return result


#print(max_independent_set([7, 2, 5, 8, 6]))
#print(max_independent_set([-1, -1, 0]))
#print(max_independent_set([-1, -1, -10, -34]))
#print(max_independent_set([10, -3, 0]))