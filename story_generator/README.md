# Random Story Generator

## Description

This Python script generates random stories by reading data from a CSV file. It pulls information from six categories: time/event, character, character name, residence, place they visited, and event that occurred. Using the `csv` and `random` modules, the script randomly selects entries from each list and combines them into a fun and creative short story.

## How It Works

- The script reads data from a CSV file (`story_data.csv`) that contains columns for time/event, who, name, residence, went, and happened.
- It stores each column in a corresponding list.
- Using a `for` loop, the script generates six random stories, selecting one item from each list for each story.
- The generated stories are printed in a readable format.


