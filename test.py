def icecreamParlor(m, arr):
    cost_map = {}
    for i, cost in enumerate(arr):
        complement = m - cost
        if complement in cost_map:
            return (cost_map[complement] + 1, i + 1)
        cost_map[cost] = i
    return None

k = 4
cost = [1, 4, 5, 3, 2]
print(icecreamParlor(k, cost))