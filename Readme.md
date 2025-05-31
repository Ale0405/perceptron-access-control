# Perceptron Access Control System

This is a Python project that simulates a simple access control system using perceptrons to evaluate login attempts and account lock status.

## Features
- Uses perceptron logic gates (AND, OR) to determine access rules.
- Tracks login attempts and blocks users after three failed attempts.
- Demonstrates the use of nested dictionaries and function decomposition in Python.

## Usage
1. Run the program with Python 3.
2. Enter a username (`Giacomo`, `Andrea`, or `Pino`).
3. If access is allowed, enter the PIN associated with the account.
4. After three incorrect attempts, the account is blocked.

## Accounts

| Username | PIN   | Attempts | Blocked |
|----------|-------|----------|---------|
| Giacomo  | 1425  | 0        | ❌      |
| Andrea   | 1564  | 1        | ❌      |
| Pino     | 1768  | 3        | ✅      |

## Requirements
- Python 3.x

## How to Run
Open your terminal and run:
```
python3 main.py
```

## Author
Alessio Amoroso