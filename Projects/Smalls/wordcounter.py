
word = str(input("Enter word: "))
letter = str(input('Enter letter to search from word: '))
count = 0

for ltr in word:
	if ltr == letter:
		count+=1

print(f"Letter '{letter}' was repeated {count} times in the word")

