from decimal import Decimal
from app.exceptions import OperationError

class OperationBase:
    name = "Base"
    def execute(self, a: Decimal, b: Decimal) -> Decimal:  # pragma: no cover
        raise NotImplementedError

class Add(OperationBase):
    name = "Addition"
    def execute(self, a, b): return a + b

class Subtract(OperationBase):
    name = "Subtraction"
    def execute(self, a, b): return a - b

class Multiply(OperationBase):
    name = "Multiplication"
    def execute(self, a, b): return a * b

class Divide(OperationBase):
    name = "Division"
    def execute(self, a, b):
        if b == 0: raise OperationError("Division by zero")
        return a / b

class Power(OperationBase):
    name = "Power"
    def execute(self, a, b):
        if b < 0: raise OperationError("Negative exponent not supported")
        return Decimal(pow(float(a), float(b)))

class Root(OperationBase):
    name = "Root"
    def execute(self, a, b):
        if b == 0: raise OperationError("Zero root undefined")
        if a < 0: raise OperationError("Root of negative not supported")
        return Decimal(pow(float(a), 1/float(b)))

class Modulus(OperationBase):
    name = "Modulus"
    def execute(self, a, b):
        if b == 0: raise OperationError("Modulus by zero")
        return a % b

class IntDivide(OperationBase):
    name = "IntDivision"
    def execute(self, a, b):
        if b == 0: raise OperationError("Division by zero")
        return Decimal(int(a // b))

class Percent(OperationBase):
    name = "Percent"
    def execute(self, a, b):
        if b == 0: raise OperationError("Percent of zero")
        return (a / b) * Decimal(100)

class AbsDiff(OperationBase):
    name = "AbsDiff"
    def execute(self, a, b):
        return abs(a - b)

class OperationFactory:
    _map = {
        "add": Add, "subtract": Subtract, "multiply": Multiply, "divide": Divide,
        "power": Power, "root": Root, "modulus": Modulus, "int_divide": IntDivide,
        "percent": Percent, "abs_diff": AbsDiff
    }

    @classmethod
    def create_operation(cls, key: str) -> OperationBase:
        op_cls = cls._map.get(key.lower())
        if not op_cls:
            raise OperationError(f"Unknown operation: {key}")
        return op_cls()
