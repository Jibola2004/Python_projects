
# 🧠 Quiz Game (Python CLI App)

This is a **command-line quiz application** built with Python. The app allows you to load quiz questions and answers from a CSV file, ask them to the user in random order, and track the user's score. Users have up to **three attempts** per question to get the correct answer.

---

## 📌 Features

- ✅ Load questions and answers from a CSV file  
- 🎲 Randomize question order for each quiz session  
- 🔁 Allow up to 3 attempts per question  
- 📈 Track and display user score at the end  
- 🗂️ Easy-to-edit CSV format for quiz content

---

## 🛠️ How It Works

1. **CSV File**: You provide a CSV file (`quiz_data.csv` by default) containing your quiz questions and answers.
2. **Start Quiz**: The quiz loads the file, shuffles the questions, and starts asking one by one.
3. **Answering**: You have 3 chances to answer each question correctly.
4. **Score**: At the end of the quiz, your total score is shown.

---

## 📁 CSV Format

Ensure your CSV file follows this structure:

```csv
Question,Answer
What is the capital of France?,Paris
What is 2 + 2?,4
What is the largest ocean?,Pacific
```

Each line must contain a `Question` and its corresponding `Answer`.

---

## ▶️ How to Run

1. Make sure you have Python installed.
2. Clone or download the project.
3. Prepare your `quiz_data.csv` file in the project directory.
4. Run the app:

```bash
python quiz.py
```

---

## 📦 Requirements

This app only uses Python standard libraries:
- `csv`
- `random`

No extra installations required.

---

## ✨ Future Improvements

- Add support for multiple-choice questions  
- Save quiz results to a file  
- Add a graphical interface (Tkinter or web-based)  
- Add timed questions or leaderboard

---

## 👨‍💻 Author

Created with ❤️ using Python.

