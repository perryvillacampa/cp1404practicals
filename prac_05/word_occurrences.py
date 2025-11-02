"""
Word Occurrences
Estimate: 30 minutes
Actual:   45 minutes
Word Counter Program

CP1404 Practical
"""


def main():
    """Reads a string and prints the sorted, aligned counts of each word."""
    text = input("Text: ")
    words = text.lower().split()
    word_to_count = {}
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1

    sorted_words = sorted(word_to_count.keys())

    max_length = 0
    if sorted_words:
        max_length = max(len(word) for word in sorted_words)

    for word in sorted_words:
        count = word_to_count[word]
        print(f"{word:{max_length}} : {count}")


main()