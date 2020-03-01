word = str(input("Type in a word "))
word_list = []
reverse_word_list = []

for a in word:
    word_list.append(a)
    print("One letter " + a)

reverse_word_list = word_list[::-1]

if(word_list == reverse_word_list):
    print("Word is a palindrome")
else:
    print("Word is not a palindrom")
