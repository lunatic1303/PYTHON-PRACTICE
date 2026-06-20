"""Problem-Printing keys and values of a dictionary""" 
v = {
    "name":"xyz",
    "age":10,
    "marks":95
}
for key,value in v.items():
    print(key,":",value)

"""Problem-Checking if key exists in dictionary"""
m = {
    "credit":100,
    "bal":265
}
n = input("Enter key to look for:")
if n in m:
    print("Key exists in dictionary")
else:
    print("Doesn't exist")

"""Problem-Finding key with max value"""
p = {
    "c":100,
    "b":265,
    "a":56
}
print("The key with maximum value is:",max(p,key=p.get))

"""Problem-Sorting dictionary by values"""
p = {
    "c":100,
    "b":265,
    "a":56
}
sor = dict(sorted(p.items(),key = lambda x : x[1]))
print(sor)

"""Problem-Counting word frequencies"""
sen = input("Enter sentence:")
words = sen.split()
freq = {}
for word in words:
    freq[word]= freq.get(word,0)+1
print(freq)

"""Problem-Merge dictionaries"""
p = {
    "c":100,
    "b":265,
    "a":56
}
v = {
    "name":"xyz",
    "age":10,
    "marks":95
}
p.update(v)
print(p)
"""Problem-Removing duplicate values from dictionary"""
b ={
    "a":10,
    "v":23,
    "n":10,
    "m":2
}
fre = {}
seen = set()
for key,value in b.items():
    if value not in seen:
        fre[key]= value
        seen.add(value)
print(fre)