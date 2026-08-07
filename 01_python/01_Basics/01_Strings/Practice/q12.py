""" 
# Count Vowels
Input :
    - Machine Learning
Output :
    - Vowels: 7
"""

text = "Machine Learning"

vowel_count = 0

for char in text.lower():
    if char in "aeiou":
        vowel_count += 1

print(f"Vowels: {vowel_count}")