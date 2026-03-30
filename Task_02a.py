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
    text = text.lower()
    if 'a' in text:
        count += text.count('a')
    if 'e' in text:
        count += text.count('e')  
    if 'i' in text:
        count += text.count('i')  
    if 'o' in text:
        count += text.count('o')  
    if 'u' in text:
        count += text.count('u') 
    
    return count
    
      


def main():
    text = input("Enter text: ")
    print(count_vowels(text))


if __name__ == "__main__":
    main()
