from dataclasses import dataclass, field
import datetime
from typing import List
from app.calculation import Calculation

@dataclass
class CalculatorMemento:
    history: List[Calculation]
    timestamp: datetime.datetime = field(default_factory=datetime.datetime.now)

    def copy(self):
        # shallow copy is fine: Calculation is immutable for our usage
        return CalculatorMemento(history=self.history.copy())
