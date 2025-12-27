# Python Flashcard CLI Application

A command-line flashcard application built from scratch in Python.  
This program allows users to create, manage, quiz, and persist flashcards using a simple menu-driven interface.

## Features
- Add flashcards (question and answer)
- View all flashcards
- Delete selected flashcards
- Quiz mode with random questions
- Automatic save and load using JSON
- Persistent storage across program runs

## Technologies Used
- Python
- JSON (for data persistence)
- Standard Python libraries (`random`, `json`)

## How It Works
- Flashcards are stored as a list of dictionaries in memory
- Each flashcard contains a question and an answer
- Flashcards are automatically loaded from a JSON file when the program starts
- Flashcards are saved back to the file when the program exits

## How to Run
1. Make sure Python is installed
2. Run the program from the terminal:

```bash
python flashcards.py
