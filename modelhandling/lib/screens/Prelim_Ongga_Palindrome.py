#Kent Gabriel Ongga - CCS 1301 CS: 526
print("Program to check if the word is Palindrome")

word = str(input("Enter a word: ")).lower()

orig_word = word
reverse_word = orig_word[::-1]

print(f"The Original word is: {orig_word}")
print(f"The reverse word is: {reverse_word}")

if orig_word == reverse_word:
    print("The word is a Palindrome")

else:
    print("The word is not a Palindrome")