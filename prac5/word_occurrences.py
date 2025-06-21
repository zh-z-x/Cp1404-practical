"""
Word Occurrences
Estimate: 20 minutes
Actual: 13 minutes
"""
# Prompt the user to enter a string
text = input("Text: ")

# Split the input text into a list of words
words = text.split()

# Create a dictionary to count occurrences of each word
word_counts = {}

# Loop over each word in the list
for word in words:
    if word in word_counts:
        word_counts[word] += 1  # Increment count if word already seen
    else:
        word_counts[word] = 1   # Initialize count if word is new

# Find the length of the longest word for alignment
max_length = max(len(word) for word in word_counts)

# Print each word and its count, sorted alphabetically and aligned nicely
for word in sorted(word_counts):
    print(f"{word:{max_length}} : {word_counts[word]}")