# Write a Python Program to Hash a Word.

soundex = [0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]

word = input("Input the Word be Hashed: ")
word = word.upper()

coded = word[0]

for a in word [1:len(word)]:
    i = 65-ord(a)
    coded = coded+str(soundex[i])
print()
print("The Coded Word is: "+coded)
print()