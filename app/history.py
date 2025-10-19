from typing import List, Protocol
from pathlib import Path
import pandas as pd
from decimal import Decimal
from app.calculation import Calculation
import os


class Observer(Protocol):
    def on_new_calculation(self, calc: Calculation):
        ...


class LoggingObserver:
    def __init__(self, logger=None):
        self.logger = logger

    def on_new_calculation(self, calc: Calculation):
        if self.logger:
            self.logger.info(
                f"{calc.operation_name}({calc.a}, {calc.b}) = {calc.result}"
            )


class AutoSaveObserver:
    def __init__(self, calculator):
        self.calculator = calculator

    def on_new_calculation(self, calc: Calculation):
        if self.calculator.config.auto_save:
            self.calculator.save_history()


def to_dataframe(history: List[Calculation]) -> pd.DataFrame:
    """Convert a list of Calculation objects to a pandas DataFrame."""
    rows = [c.to_row() for c in history]
    return pd.DataFrame(rows, columns=["operation", "a", "b", "result", "timestamp"])


def save_history(history: List[Calculation], filepath: str | Path):
    """Save calculation history to a CSV file."""
    df = to_dataframe(history)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)


def load_history(filepath: str | Path) -> List[Calculation]:
    """Load calculation history from a CSV file."""
    if not os.path.exists(filepath):
        return []

    try:
        df = pd.read_csv(filepath)
        history = [
            Calculation(
                row["operation"],
                Decimal(str(row["a"])),
                Decimal(str(row["b"])),
                Decimal(str(row["result"])),
            )
            for _, row in df.iterrows()
        ]
        return history
    except Exception:
        return []



