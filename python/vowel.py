s="interview"
vowels="aeiou"
count=sum(1 for ch in s if ch in vowels)
print(count)

#find common character between two strings
a="apple"
b="grapes"
common=set(a)&set(b)
print(common)

#expand a compressed string
s="a3b2c5"
result=""
for i in range(0,len(s),2):
char=s[i]


