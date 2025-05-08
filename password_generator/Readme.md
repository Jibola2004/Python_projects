# 🔐 Password Generator Script

## 📋 Description

This Python script generates a random password based on the length specified by the user. It ensures the user inputs a valid integer for the password length and constructs a password using a mix of:

- Lowercase letters (`a-z`)
- Uppercase letters (`A-Z`)
- Digits (`0-9`)
- Special characters (`!.,?;:><#+-*$^@`)

The password is printed at the end of execution.

---

## ✅ Features

- User-defined password length.
- Input validation to ensure the input is an integer.
- Random selection of characters from a secure set.

---

## 🧠 How It Works

1. Prompts the user for the desired password length.
2. Converts the `choices` string (which contains all allowed characters) into a list.
3. Iterates `number` times, each time adding a randomly selected character from the list to the result.
4. Displays the final password.
