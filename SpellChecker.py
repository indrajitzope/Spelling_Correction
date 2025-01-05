from spellchecker import SpellChecker

# Initialize the spell checker
spell = SpellChecker()

# Example text
words = ["speling", "errurs", "somthing", "writen", "bee", "corected", "easly"]

# Find misspelled words
misspelled = spell.unknown(words)

# Correct each misspelled word
for word in misspelled:
    print(f"Original: {word}, Corrected: {spell.correction(word)}")
