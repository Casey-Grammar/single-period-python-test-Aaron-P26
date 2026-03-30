# Task 04 - Expand Subject Codes
# Write a function called expand_subject_codes(codes)
# that takes a list of short subject codes and returns a new list
# with the full subject names.
#
# Use the following code table:
# ENG -> English
# MAT -> Mathematics
# SCI -> Science
# HIS -> History
# ART -> Art
#
# If a code is not recognised, ignore it.
#
# Example:
# expand_subject_codes(["MAT", "SCI", "XYZ", "ENG"])
# returns ["Mathematics", "Science", "English"]

def expand_subject_codes(codes):
    # Write your code here
    full_names = []

    for code in codes:
        if code == 'ENG':
            full_names.append("English")
        if code == 'MAT':
            full_names.append("Mathematics")
        if code == 'SCI':
            full_names.append("Science")
        if code == 'HIS':
            full_names.append("History")
        if code == 'ART':
            full_names.append("Art")
    return full_names

def main():
    user_input = input("Enter subject codes separated by commas: ")
    codes = [code.strip().upper() for code in user_input.split(",") if code.strip() != ""]
    print(expand_subject_codes(codes))


if __name__ == "__main__":
    main()
