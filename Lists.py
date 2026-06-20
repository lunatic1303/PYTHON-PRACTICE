"""Problem-Finding largest and smallest element in list"""
l = [3,5,1,9,2]
print("Largest element:",max(l))
print("Smallest element:",min(l))

"""Problem-Second largest element in list"""
l = [3,5,1,9,2]
l.sort()
print("The second largest element is:",l[-2])

"""Problem-Removing duplicates from list"""
m = [1,2,6,7,2,6,4,1]
print(set(m))

"""Problem-Merging two lists"""
l1 = [10,20,30]
l2 = [40,50,60]
print(l1+l2)

"""Problem-Finding common elements"""
l1 = [10,20,30]
l2 = [40,50,60,10,20]
o = l1 + l2
q = []
for el in o:
    if o.count(el)>1:
        q.append(el)
print("Common elements are:",set(q))

"Problem-Rotate a list"
m1 = [10,20,30,40]
k = int(input("Enter number of rotations:"))
k = k%len(m1)
print(m1[-k:]+m1[:-k])

"""Problem-First repeated element in list"""
b = [1,2,6,4,5,1,4]
for ml in b:
    if b.count(ml)>1:
        print("First repeated element is",ml)
        break


