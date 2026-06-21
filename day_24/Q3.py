# Program to find the longest word in a sentence

sentence = input("Enter a sentence: ")

words = sentence.split()

longest = max(words, key=len)

print("Longest word:", longest)