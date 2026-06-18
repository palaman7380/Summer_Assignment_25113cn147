s = input("Enter a string: ").lower()

vowels = 0
consonants = 0

for ch in s:
    if ch.isalpha():  # check if letter
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)