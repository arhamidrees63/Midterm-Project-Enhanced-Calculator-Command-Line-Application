# 🧮 Advanced Calculator (Midterm Project)

## 📘 Project Overview
This project is an **Advanced Command-Line Calculator** developed as part of the **IS601 Midterm Project**.  
It implements object-oriented design principles and multiple software design patterns, including **Factory**, **Memento**, and **Observer**, with additional features such as **Undo/Redo**, **Logging**, **History Management**, and **CI/CD automation** through GitHub Actions.

The calculator supports both **basic arithmetic** and **advanced operations**, offers **robust error handling**, and saves its history automatically using `pandas`.

---

## 🏗️ Project Structure
midterm_calculator/
├── app/
│ ├── calculator.py
│ ├── calculation.py
│ ├── calculator_config.py
│ ├── calculator_memento.py
│ ├── exceptions.py
│ ├── history.py
│ ├── input_validators.py
│ ├── operations.py
│ ├── logger.py
│ └── calculator_repl.py
├── tests/
│ ├── test_calculator.py
│ ├── test_calculation.py
│ ├── test_history.py
│ └── test_operations.py
├── main.py
├── requirements.txt
├── .env
└── .github/
└── workflows/
└── python-app.yml

yaml
Copy code

---

## ⚙️ Installation Instructions

### 1️⃣ Create and Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
2️⃣ Install Dependencies
bash
Copy code
pip install --upgrade pip
pip install -r requirements.txt
If you don’t have a requirements.txt yet, create one with:

bash
Copy code
pip freeze > requirements.txt
🧮 Usage Instructions
Run the Calculator
From your terminal inside the project folder:

bash
Copy code
python main.py
You’ll see:

pgsql
Copy code
=======================================
   🧮 Advanced Calculator (Midterm)
=======================================
Type 'help' to see available commands.
Type 'exit' to quit.
Example Commands
pgsql
Copy code
add 5 3           → 8
subtract 10 6     → 4
multiply 2 4      → 8
divide 10 2       → 5
power 2 5         → 32
root 27 3         → 3
modulus 10 3      → 1
int_divide 10 3   → 3
percent 5 100     → 5
abs_diff 7 2      → 5
history           → Show past operations
undo              → Undo last operation
redo              → Redo previous undone operation
clear             → Clear all history
save              → Save calculation history to CSV
load              → Load previous history
exit              → Quit the calculator
🧩 Design Patterns Implemented
Pattern	Description
Factory	Creates operation objects dynamically based on user input
Memento	Enables Undo and Redo functionality by saving previous calculator states
Observer	Handles automatic logging and history-saving when calculations occur

⚡ CI/CD Automation (GitHub Actions)
A workflow .github/workflows/python-app.yml runs automatically when code is pushed to GitHub.
It performs the following:

Installs dependencies

Runs all pytest unit tests

Enforces 90% or higher code coverage

🧪 Testing
Run tests manually with:

bash
Copy code
pytest --cov=app
You should see output like:

Copy code
11 passed in 1.5s
🧠 Key Learning Outcomes
✅ Git version control and branching

✅ Use of Linux & Python virtual environments

✅ Object-oriented Python application design

✅ Automated testing & coverage

✅ GitHub Actions (CI/CD)

✅ Advanced command-line user interface

✅ Application of Factory, Memento, and Observer patterns

✅ Data persistence using pandas

🏅 Author
Muhammad Arham