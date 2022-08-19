'''
#Properties of Sets
    1. Sets are unordered       => Elements order doesn't matter
    2. Sets are unindexed
    3. There is no way to change items in sets
    4. Sets cannot contain duplicate values
'''
# S = set()
# S.add(3)
# S.add(1)
# S.add(1)
# S.add(2)
# S.add(2)
# S.add(6)
# S.add(5)
# print(S)






mySet = {1,34,53}
mySet.add(45)
mySet.add("1")
print(mySet)

mySet.remove(34)
mySet.add("1")
print(mySet)

print(mySet.pop())
print(mySet)

print(len(mySet))


print(mySet.union({1,2,3,4,5,6,7}))         #union of sets
print(mySet.intersection({1,"1", 45}))      #intersection of sets


mySet.clear()










