""""Problem-Reverse a string"""
v = input("Enter string:")
print("Reversed string is", v[::-1])

"""Problem-Palindrome checker"""
m = input("Enter string:")
if m == m[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

"""Problem-Count vowels and consonants in a string"""
n = input("Enter string:")
vowels = 0
conso = 0
for el in n.lower():
    if el in "aeiou":
        vowels += 1
    elif el.isalpha():
        conso += 1
print("Number of vowels:",vowels)
print("Number of consonants:",conso)

"""Problem-Count words in a sentence"""
sentence = input("Enter sentence:")
words = sentence.split()
print("Number of words:", len(words))

""""Problem-Most frequent character in string"""
s = input("Enter string:")
freq = {}
for ch in s:
    freq[ch]= freq.get(ch,0)+1
    max_char = max(freq,key = freq.get)
print("The most frequent character is",max_char)

"""Problem-Remove spaces from sentence"""
sen = input("Enter sentence:")
print("Sentence after removing spaces:",sen.replace(" ",""))

"""Problem-Checking anagrams"""
s1 = input("Enter first sentence:")
s2 = input("Enter second sentence:")
if sorted(s1.lower())==sorted(s2.lower()):
    print("Anagrams")
else:    
    print("Not anagrams")
