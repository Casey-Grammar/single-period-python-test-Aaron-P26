# Task 02a - Count Vowels
# Write a function called count_vowels(text)
# that returns the number of vowels in the string.
# Count both uppercase and lowercase vowels.
#
# Vowels are: a, e, i, o, u
#
# Example:
# count_vowels("Education") -> 5

def count_vowels(text):
    # Write your code here
    count = 0
    if 'a' in text.lower():
        count += text.lower().count('a')
    if 'e' in text.lower:
        count += text.lower().count('e')
    if 'i' in text.lower:
        count += text.lower().count('i')
    if 'o' in text.lower:
        count += text.lower().count('o')
    if 'u' in text.lower:
        count += text.lower().count('u')
    return count
      


def main():
    text = input("Enter text: ")
    print(count_vowels(text))


if __name__ == "__main__":
    main()
