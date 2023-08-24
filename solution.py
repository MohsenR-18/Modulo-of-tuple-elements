# initializing tuples
tuple1 = (10, 4, 5, 6)
tuple2 = (5, 6, 7, 5)

# creating modulus_tuple
mList = []
for i in range(len(tuple1)):
    mList.append(tuple1[i]%tuple2[i])

modulus_tuple = tuple(mList)

# printing results
print("The original tuple 1: " + str(tuple1))
print("The original tuple 2: " + str(tuple2))
print("The modulus tuple: " + str(modulus_tuple))
