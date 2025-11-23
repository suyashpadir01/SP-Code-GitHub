def check_vowel(ch):
    vowels = "aeiouAEIOU"
    if ch in vowels:
        return "Vowel"
    else:
        return "Not a Vowel or its a consonant"

c = input("Enter a character: ")
print(check_vowel(c))
