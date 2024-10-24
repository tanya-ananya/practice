s1 = set({1,2,2,4,4,5})
s2 = {4,5,5,6}
s2.add(7) #add new item
s2.remove(6) #remove existing item
print('set 1 = ',s1)
print('set 2 =', s2)
print('union - ',s1.union(s2))
print('intersection - ',s1.intersection(s2))
print('is disjoint? - ',s1.isdisjoint(s2))
print(10 in s2) #membership test

'''Use set to remove duplicates from a list'''
def checker(lst):
    set_list = set(lst)
    lst = []
    for x in set_list:
        lst.append(x)
    return lst

print(checker([1, 2,2,3, 3, 4, 4,7]))