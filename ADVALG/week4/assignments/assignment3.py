
# knapsack unbounded - Greedy approach

def knapsack(v, w, cap):
    rwv = []         # triplet ratio, weight, value, index
    for i in range(len(v)):
        rwv.append([v[i]/w[i],w[i],v[i],i])
    rwv.sort(reverse=True)    # sort from high to low rate
    ans = []                     # the list of added items
    tw = 0                                  # total weight
    found = True
    while (found):        # until no fitting item is found
        found = False
        for t in rwv:              # search an item to add
            if (t[1] + tw) <= cap:      # if the item fits
                ans.append(t[3])                  # add it
                tw += t[1]
                found = True
                break
    return ans           # returns the list of added items

def main():

    # creating a data stuct to hold capacity as well as value and weight.
    info = [
        [[838],[[5,10],[8,20],[12,30]]],
        [[997],[[3,17],[5,23],[7,29],[11,31],[13,37]]],
        [[250],[[5,25],[6,36],[7,49],[8,64]]],
        [[360],[[5,25],[6,36],[7,49],[8,64]]]
        ]

    # step1, get index 0 for each to get capacity
    # step2, get index 1 length for the number of items.
    # step3, iterate over index 1, where item 1 is value and 2 is weight

    items = int(len(info))
    values, weights = [],[]
    for i in info:
        values = []
        weights = []
        weightValues = i[1]
        for y in weightValues:
            values.append(y[0])
            weights.append(y[1])

        capacity = i[0][0]
        answer = knapsack(values, weights, capacity)
        tv, tw = 0, 0
        for a in answer:
            print("Item - Value:", values[a], "- Weight:", weights[a])
            tv += values[a]
            tw += weights[a]
        print("Items:", len(answer), "- Value:", tv, "- Weight:", tw)

main()
