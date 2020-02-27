word = str(input("Type in a word "))
wordList = []
reverseWordList = []

for a in word:
    wordList.append(a)
    print("One letter " + a)

reverseWordList = wordList[::-1]

if(wordList == reverseWordList):
    print("Word is a palindrome")
else:
    print("Word is not a palindrom")
