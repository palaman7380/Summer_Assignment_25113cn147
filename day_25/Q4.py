# Program to sort words according to their length

words = input("Enter words separated by space: ").split()

words.sort(key=len)

print("Words sorted by length:")
print(words)