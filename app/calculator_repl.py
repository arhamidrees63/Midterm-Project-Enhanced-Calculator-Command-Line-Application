from decimal import Decimal
from app.calculator import Calculator
from app.history import LoggingObserver, AutoSaveObserver
from app.operations import OperationFactory
from app.exceptions import ValidationError
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def calculator_repl():
    calc = Calculator()
    calc.add_observer(LoggingObserver())
    calc.add_observer(AutoSaveObserver(calc))


    print(Fore.CYAN + "Calculator started. Type 'help' for available commands.\n")

    while True:
        cmd = input(Fore.YELLOW + "\nEnter command: ").strip().lower()

        # ---------------- HELP ----------------
        if cmd == "help":
            print(Fore.GREEN + """
Available Commands:
────────────────────────────────────────────
 add [a] [b]           → Add two numbers
 subtract [a] [b]      → Subtract b from a
 multiply [a] [b]      → Multiply two numbers
 divide [a] [b]        → Divide a by b
 power [a] [b]         → a raised to the power of b
 root [a] [b]          → b-th root of a
 modulus [a] [b]       → Remainder of a divided by b
 int_divide [a] [b]    → Integer division of a/b
 percent [a] [b]       → (a / b) * 100
 abs_diff [a] [b]      → Absolute difference
────────────────────────────────────────────
 history               → Show calculation history
 undo                  → Undo last operation
 redo                  → Redo undone operation
 save                  → Save calculation history
 load                  → Load previous history
 clear                 → Clear current history
 exit                  → Exit the calculator
            """)
            continue

        # ---------------- EXIT ----------------
        if cmd == "exit":
            try:
                calc.save_history()
            except Exception:
                pass
            print(Fore.MAGENTA + "\n👋 Exiting Calculator. Goodbye!")
            break

        # ---------------- HISTORY ----------------
        if cmd == "history":
            rows = calc.show_history()
            if not rows:
                print(Fore.YELLOW + "No history found.")
            else:
                print(Fore.CYAN + "\n📜 History:")
                for i, r in enumerate(rows, 1):
                    print(Fore.WHITE + f"{i}. {r}")
            continue

        # ---------------- CLEAR ----------------
        if cmd == "clear":
            calc.history.clear()
            print(Fore.BLUE + "🧹 History cleared.")
            continue

        # ---------------- UNDO / REDO ----------------
        if cmd == "undo":
            print(Fore.GREEN + "Undo: ✅ Success" if calc.undo() else Fore.RED + "⚠️ Nothing to undo.")
            continue

        if cmd == "redo":
            print(Fore.GREEN + "Redo: ✅ Success" if calc.redo() else Fore.RED + "⚠️ Nothing to redo.")
            continue

        # ---------------- SAVE / LOAD ----------------
        if cmd == "save":
            calc.save_history()
            print(Fore.CYAN + "💾 History saved successfully.")
            continue

        if cmd == "load":
            calc.load_history()
            print(Fore.CYAN + "📂 History loaded successfully.")
            continue

        # ---------------- OPERATIONS ----------------
        try:
            parts = cmd.split()
            if len(parts) != 3:
                print(Fore.RED + "⚠️ Format: <operation> <a> <b>")
                continue

            op, a_text, b_text = parts
            calc.set_operation(OperationFactory.create_operation(op))
            result = calc.perform_operation(a_text, b_text)
            print(Fore.GREEN + f"✅ {op.capitalize()} result: {result}")

        except ValidationError as ve:
            print(Fore.RED + "❌ Validation error: " + str(ve))
        except Exception as e:
            print(Fore.RED + "❌ Error: " + str(e))
