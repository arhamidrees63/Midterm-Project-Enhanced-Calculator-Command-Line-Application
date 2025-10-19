from decimal import Decimal
from pathlib import Path
from typing import List
import pandas as pd

from app.calculation import Calculation
from app.calculator_config import CalculatorConfig
from app.calculator_memento import CalculatorMemento
from app.exceptions import ValidationError, OperationError
from app.input_validators import to_decimal
from app.operations import OperationBase, OperationFactory
from app.history import to_dataframe, Observer
from app.logger import get_logger

class Calculator:
    def __init__(self, config: CalculatorConfig | None = None):
        self.config = config or CalculatorConfig.load()
        self.config.history_dir.mkdir(parents=True, exist_ok=True)
        self.config.log_dir.mkdir(parents=True, exist_ok=True)
        self._logger = get_logger(self.config.log_dir)
        self.history: List[Calculation] = []
        self._observers: List[Observer] = []
        self._undo_stack: List[CalculatorMemento] = []
        self._redo_stack: List[CalculatorMemento] = []
        self._current_op: OperationBase | None = None

    # Observer handling
    def add_observer(self, obs: Observer):
        self._observers.append(obs)

    def _notify(self, calc: Calculation):
        for o in self._observers:
            o.on_new_calculation(calc)

    # Operation handling
    def set_operation(self, operation: OperationBase):
        self._current_op = operation

    def perform_operation(self, a_text: str, b_text: str) -> Decimal:
        if not self._current_op:
            raise OperationError("No operation set")

        a = to_decimal(a_text, self.config.max_input_value)
        b = to_decimal(b_text, self.config.max_input_value)

        # Save undo point
        self._undo_stack.append(CalculatorMemento(self.history.copy()))
        self._redo_stack.clear()

        result = self._current_op.execute(a, b)
        calc = Calculation(self._current_op.name, a, b, result)
        self.history.append(calc)
        if len(self.history) > self.config.max_history_size:
            self.history.pop(0)

        self._logger.info(f"{calc.operation_name}({a}, {b}) = {result}")
        self._notify(calc)
        return result

    # History helpers
    def show_history(self) -> List[str]:
        return [f"{c.operation_name}({c.a}, {c.b}) = {c.result}" for c in self.history]

    def clear_history(self):
        self.history.clear()
        self._undo_stack.clear()
        self._redo_stack.clear()

    # Undo/Redo
    def undo(self) -> bool:
        if not self._undo_stack:
            return False
        m = self._undo_stack.pop()
        self._redo_stack.append(CalculatorMemento(self.history.copy()))
        self.history = m.history.copy()
        return True

    def redo(self) -> bool:
        if not self._redo_stack:
            return False
        m = self._redo_stack.pop()
        self._undo_stack.append(CalculatorMemento(self.history.copy()))
        self.history = m.history.copy()
        return True

    # Persistence (pandas)
    def _history_file(self) -> Path:
        return self.config.history_dir / "history.csv"

    def save_history(self):
        df = to_dataframe(self.history)
        df.to_csv(self._history_file(), index=False, encoding=self.config.default_encoding)

    def load_history(self):
        f = self._history_file()
        if not f.exists():
            return
        df = pd.read_csv(f, dtype=str, encoding=self.config.default_encoding)
        self.history = [Calculation.from_row(r) for _, r in df.iterrows()]
        self._undo_stack.clear()
        self._redo_stack.clear()
