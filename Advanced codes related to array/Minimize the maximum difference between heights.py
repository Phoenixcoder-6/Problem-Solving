def minimize_max_diff(heights, k):
    n = len(heights)
    if n == 1:
        return 0  # If there's only one tower, the difference is 0

    # Sort the array
    heights.sort()

    # The initial maximum difference without any modifications
    max_diff = heights[-1] - heights[0]

    # Initial smallest and largest heights after modification
    small = heights[0] + k
    large = heights[-1] - k

    # Swap if needed to ensure small <= large
    if small > large:
        small, large = large, small

    # Traverse the array and adjust the small and large values
    for i in range(1, n - 1):
        subtract = heights[i] - k
        add = heights[i] + k

        # If both the subtract and add operations keep the value within small and large
        if subtract >= small or add <= large:
            continue

        # Choose the best option between shrinking the range or expanding it minimally
        if large - subtract <= add - small:
            small = subtract
        else:
            large = add

    return min(max_diff, large - small)

# Example usage
heights = [1, 15, 10]
k = 6
print("Minimum difference:", minimize_max_diff(heights, k))
