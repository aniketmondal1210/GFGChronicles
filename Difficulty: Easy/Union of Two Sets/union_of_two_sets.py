a = set([int(x) for x in input().strip().split()])
b = set([int(x) for x in input().strip().split()])

########### Write your code below ###############
st = a.union(b)

########### Write your code above ###############

# Printing the size of the set which is the total number of elements in the set.
print(len(st))
