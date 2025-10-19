from typing import List, Protocol
from pathlib import Path
import pandas as pd
from app.calculation import Calculation

class Observer(Protocol):
    def on_new_calculation(self, calc: Calculation): ...

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
    rows = [c.to_row() for c in history]
    return pd.DataFrame(rows, columns=["operation", "a", "b", "result", "timestamp"])
