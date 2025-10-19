from decimal import Decimal, InvalidOperation
from app.exceptions import ValidationError

def to_decimal(value: str, max_value: int = 1000000) -> Decimal:
    """Convert a string to Decimal and validate its range."""
    try:
        num = Decimal(value)
    except (InvalidOperation, ValueError):
        raise ValidationError(f"Invalid number: {value}")

    if abs(num) > max_value:
        raise ValidationError(f"Value {num} exceeds maximum allowed {max_value}")

    return num
