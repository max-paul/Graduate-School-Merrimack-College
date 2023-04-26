def knapsack(items, max_volume):
    # Initialize the dynamic programming table
    table = [[0] * (max_volume + 1) for _ in range(len(items) + 1)]
    # Iterate over each item and fill in the table
    for i, item in enumerate(items):
        name, price, height, width, depth = item
        for j in range(1, max_volume + 1):
            if height * width * depth > j:
                table[i+1][j] = table[i][j]
            else:
                table[i+1][j] = max(table[i][j], table[i][j-height*width*depth] + price)

    # Backtrack to find the selected items
    selected_items = []
    i, j = len(items), max_volume
    while i > 0 and j > 0:
        if table[i][j] != table[i-1][j]:
            name, price, height, width, depth = items[i-1]
            selected_items.append((name, price))
            j -= height * width * depth
        i -= 1

    # Return the maximum total value and the selected items
    return table[-1][-1], selected_items

