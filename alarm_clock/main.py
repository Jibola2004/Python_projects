from datetime import datetime
from time import sleep
import pygame

# Initialize pygame mixer
pygame.init()
pygame.mixer.init()

# Load the audio file
pygame.mixer.music.load("My_Love.mp3")

# Get user input
time_input = input('⏰ Set your alarm (format: HH:MM:SS): ')

# Validate input
if not time_input.strip():
    raise ValueError('Invalid input. Please enter a valid time.')

try:
    alarm_time = datetime.strptime(time_input.strip(), "%H:%M:%S").time()
except ValueError:
    raise ValueError("Time format must be HH:MM:SS")

print(f"✅ Alarm set for {alarm_time.strftime('%H:%M:%S')}")

# Check the time every second
while True:
    current_time = datetime.now().time()
    if (current_time.hour == alarm_time.hour and
        current_time.minute == alarm_time.minute and
        current_time.second == alarm_time.second):
        print("⏰ Time's up!")
        pygame.mixer.music.play()
        break
    sleep(1)

# Keep playing until sound finishes
while pygame.mixer.music.get_busy():
    sleep(1)
