def fractional_knapsack(profit, weight, capacity):
    n = len(profit)

    items = sorted(
        range(n),
        key=lambda i: profit[i] / weight[i],
        reverse=True
    )

    total_profit = 0

    for i in items:
        if capacity == 0:
            break

        if weight[i] <= capacity:
            total_profit += profit[i]
            capacity -= weight[i]
        else:
            fraction = capacity / weight[i]
            total_profit += profit[i] * fraction
            capacity = 0

    return total_profit


n = int(input("Enter number of objects: "))

profit = list(map(int, input("Enter profits: ").split()))

weight = list(map(int, input("Enter weights: ").split()))

capacity = int(input("Enter knapsack capacity: "))

result = fractional_knapsack(profit, weight, capacity)

print("Maximum profit:", result)
