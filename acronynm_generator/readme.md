## Acronym Generator

This program generates an acronym from a given phrase.

An **acronym** is a shortened form created by taking the first letter of each word in a phrase — for example, **NLP** stands for *Natural Language Processing*.

### How It Works:
- The program takes a phrase as input from the user.
- If the input is empty or consists only of whitespace, it raises a `ValueError`.
- Otherwise, it:
  - Splits the phrase into individual words.
  - Extracts the first character from each word.
  - Converts each character to uppercase.
  - Combines the characters to form and return the acronym.

### Example:
- Input: "Central Processing Unit"
- Output: "CPU"