# ✊✋✌ Rock-Paper-Scissors Game

## 📋 Description
This is a Python terminal-based implementation of the classic **Rock-Paper-Scissors** game, where the user plays against the computer. The game continues until either the user or the computer wins 3 rounds.

## ✅ Features
- Takes input from the user (1 for Rock, 2 for Paper, 3 for Scissors, 4 to Exit).
- Random choice generation for the computer each round.
- Tracks and displays score after each round.
- Declares the winner after 3 victories.
- Validates input to prevent crashes.

## 🧠 How It Works
1. The game uses a `tuple` of `(number, name)` pairs to represent each move.
2. Inside the `while` loop:
   - User is prompted for a choice.
   - The computer randomly chooses its move (done **inside** the loop to ensure it changes each round ✅).
   - Both choices are compared to determine the round's winner.
3. The score is updated after each round.
4. The game ends when either the user or computer reaches 3 points.

## 📦 Requirements
- Python 3.x (no additional libraries needed)


