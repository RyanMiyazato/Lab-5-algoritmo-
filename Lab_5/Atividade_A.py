def min_months_to_water(k, growth):
    growth.sort(reverse=True)  # Sort growth in descending order
    total_growth = 0
    months = 0

    if k == 0:
        return 0  # No watering needed if k is 0

    for g in growth:
        total_growth += g
        months += 1
        if total_growth >= k:
            return months  # Minimum months required

    return -1  # If even after all months we don't reach k


# Read input
k = int(input().strip())
growth = list(map(int, input().strip().split()))

# Output the result
print(min_months_to_water(k, growth))
