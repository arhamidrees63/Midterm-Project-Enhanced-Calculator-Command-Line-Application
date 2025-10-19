from decimal import Decimal, InvalidOperation
from app.exceptions import ValidationError

def to_decimal(text: str, max_abs: float) -> Decimal:
    try:
        d = Decimal(str(text))
    except (InvalidOperation, ValueError):
        raise ValidationError(f"Not a number: {text}")
    if abs(float(d)) > max_abs:
        raise ValidationError(f"Value too large: {text}")
    return d
