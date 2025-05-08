
# ⏰ Python Alarm Clock

## Requirements

1. Set up a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```

2. Install pygame:
   ```bash
   pip install pygame
   ```

3. Download and place an MP3 file (e.g., `My_Love.mp3`) in the project directory.

## Description

This project allows you to set an alarm in the format `HH:MM:SS`.  
- If the input is empty or not in the correct format, the program raises a `ValueError`.
- Once a valid time is provided, the script continuously checks the system time.
- When the current time matches the set alarm, it plays the specified MP3 file using the `pygame` mixer.
