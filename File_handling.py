"""Problem-Write multiplication table to a file"""
with open("sample.txt","w") as f:
    n = input("Enter a number:")
    for i in range(1,11):
        f.write(f"{n} X {i} = {int(n)*i}\n")

"""Problem-Read content from a file"""
with open("sample.txt","r") as f:
    data = f.read()
    print(data)

"""Problem-Count lines in a file"""
with open("sample.txt","r") as f:
    n = f.readlines()
    print("Number of lines in file:",len(n))

"""Problem-Write user input to a file"""
with open("varsh.txt","w") as m:
    m.write("I am super shy girl")

"""Problem-Count words in a file"""
with open("varsh.txt","r") as k:
    w = k.read()
    words = w.split()
    print("Number of words in a file is:",len(words))

"""Problem-Copy content from one file to another"""
with open("varsh.txt","r") as f1:
    data1 = f1.read()
with open("Copy.txt","w") as f2:
    f2.write(data1)