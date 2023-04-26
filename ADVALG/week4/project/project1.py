# This function reads data from a file and calculates the total volume of all items
# then sorts them by value in descending order
# it then uses the knapsack algorithm to select the items to be included in the knapsack
# based on their value and volume, and calculates the total value and volume of the selected items.
from knapsack import knapsack

def main():
    filename = 'sample.txt' # the file name to read data from
    max_vol = 0 # the total volume of all items read from the file

    items = [] # an empty list to store the information of the items
    with open(filename) as f:
        for line in f:
            item = line.strip().split(",") # each line contains information about an item, which is separated by a comma
            name = item[0] # the name of the item
            value = int(item[1]) # the value of the item
            height = int(item[2]) # the height of the item
            width = int(item[3]) # the width of the item
            depth = int(item[4]) # the depth of the item
            volume = height * width * depth # the volume of the item
            items.append((name, value, volume)) # add the item's information to the list of items
            max_vol += volume # add the volume of the current item to the total volume

    items = sorted(items, key=lambda x: x[1], reverse=True) # sort the items by their values in descending order
    ans = knapsack([i[1] for i in items], [i[2] for i in items], max_vol) # use the knapsack algorithm to select the items to be included in the knapsack
    selected_items = [items[i] for i in ans] # create a list of the selected items
    total_value = sum([i[1] for i in selected_items]) # calculate the total value of the selected items
    total_volume = sum([i[2] for i in selected_items]) # calculate the total volume of the selected items
    unused_volume = max_vol - total_volume # calculate the unused volume in the knapsack

    # print the total number of selected items, total value, total volume, and unused volume in the knapsack
    print(f"Total items: {len(selected_items)}; total value: {total_value}; total volume: {total_volume}; total unused volume: {unused_volume}")
    # print the names of the selected items
    print([i[0] for i in selected_items])


if __name__ == "__main__":
    main()

