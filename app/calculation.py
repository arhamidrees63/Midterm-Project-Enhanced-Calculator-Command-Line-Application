from decimal import Decimal
from datetime import datetime

class Calculation:
    """Represents a single arithmetic calculation with result tracking."""

    def __init__(self, operation_name: str, a: Decimal, b: Decimal, result: Decimal):
        self.operation_name = operation_name
        self.a = a
        self.b = b
        self.result = result
        self.timestamp = datetime.now()

    @classmethod
    def create(cls, operation_name, a, b, result):
        """Factory method to create a Calculation object."""
        return cls(operation_name, a, b, result)

    def to_dict(self):
        """Convert calculation data to a dictionary."""
        return {
            "operation": self.operation_name,
            "a": str(self.a),
            "b": str(self.b),
            "result": str(self.result),
            "timestamp": self.timestamp.isoformat()
        }

    def to_row(self):
        """Return a tuple representing this calculation (used in CSV/DF conversion)."""
        return (
            self.operation_name,
            str(self.a),
            str(self.b),
            str(self.result),
            self.timestamp.isoformat()
        )

    @classmethod
    def from_row(cls, row):
        """Create a Calculation instance from a CSV/DF row."""
        op_name, a, b, result, timestamp = row
        c = cls(op_name, Decimal(a), Decimal(b), Decimal(result))
        c.timestamp = datetime.fromisoformat(timestamp)
        return c

    def __repr__(self):
        return f"{self.operation_name}: {self.a} and {self.b} = {self.result}"

    @property
    def operation(self):
         """Alias for backward compatibility in tests."""
         return self.operation_name
