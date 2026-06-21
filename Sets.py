"""Problem-Union of sets"""
a={1,2,4,5}
b={2,3,6,2}
print(a.union(b))

"""Problem-Intersection of sets"""
a={1,2,4,5}
b={2,3,6,2}
print(a.intersection(b))

"""Problem-Difference of sets"""
a={1,2,4,5}
b={2,3,6,2}
print(a.difference(b))

"""Problem-Symmetric difference of sets"""
a={1,2,4,5}
b={2,3,6,2}
print(a.symmetric_difference(b))

"""Problem-Finding unique elements in a list"""
m = [1,2,3,4,1,5,2]
q = set()
for el in m:
    if m.count(el)<=1:
        q.add(el)
print("Unique elements are:",q)

"""Problem-Find common elements between two lists"""
l1 = [10,20,30]
l2 = [40,50,60,10,20]
o = set(l1)&set(l2)
print(o)

        