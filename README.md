🧮 Advanced Calculator — Midterm Project
Author: Muhammad Arham
📘 Overview

This project is an enhanced command-line calculator built as part of the Midterm Project.
It demonstrates object-oriented design, software engineering patterns, and CI/CD automation through GitHub Actions.

The calculator supports various arithmetic operations, a REPL interface, undo/redo history, logging, and auto-save functionality using pandas.

⚙️ Features
🔹 Core Arithmetic

Addition, Subtraction, Multiplication, Division

Power (a^b), Root (b-th root of a)

Modulus (remainder)

Integer Division (a // b)

Percentage ((a / b) * 100)

Absolute Difference (|a - b|)

🔹 Advanced Functionality

Undo / Redo using Memento Pattern

Auto-save and logging via Observer Pattern

Operation creation via Factory Pattern

Robust input validation and error handling

Persistent history saved as .csv using pandas

Configurable environment variables using .env

🧠 Design Patterns Used
Pattern	Purpose	Example
Factory	Dynamically creates operation objects	OperationFactory.create_operation()
Observer	Notifies loggers and auto-savers when a calculation occurs	LoggingObserver, AutoSaveObserver
Memento	Enables Undo/Redo by storing calculator states	CalculatorMemento
🧩 Project Structure
midterm_calculator/
│
├── app/
│   ├── calculator.py
│   ├── calculation.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── calculator_repl.py
│   ├── history.py
│   ├── operations.py
│   ├── input_validators.py
│   ├── logger.py
│   └── exceptions.py
│
├── tests/
│   ├── test_calculator.py
│   ├── test_calculation.py
│   ├── test_history.py
│   └── test_repl_and_utilities.py
│
├── .github/workflows/python-app.yml
├── requirements.txt
├── .env
└── README.md

🧪 Testing and CI/CD

Unit tests written using pytest

Coverage measurement with pytest-cov

CI pipeline runs automatically via GitHub Actions

Enforces a minimum 90% test coverage

To run tests locally:

pytest --cov=app

💻 Running the Calculator (REPL)

Start the calculator from your terminal:

python main.py


You’ll see:

=======================================
   🧮 Advanced Calculator (Midterm)
=======================================
Type 'help' to see available commands.
Type 'exit' to quit.

Example session:
Enter command: add 5 10
✅ Add result: 15

Enter command: power 2 3
✅ Power result: 8

Enter command: history
1. Addition(5, 10) = 15
2. Power(2, 3) = 8

Enter command: undo
Operation undone

Enter command: redo
Operation redone

Enter command: exit
👋 Exiting Calculator. Goodbye!

🧰 Technologies Used

Python 3.12

pytest / pytest-cov

pandas

python-dotenv

GitHub Actions for CI/CD

🏁 Learning Outcomes

This project demonstrates:

Mastery of Git & GitHub workflows

Implementation of OOP principles and design patterns

Integration of CI/CD pipelines for quality assurance

Use of Python REPL for interactive applications