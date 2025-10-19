from decimal import Decimal
from app.calculation import Calculation

def test_calc_row_roundtrip():
    c = Calculation("Addition", Decimal("2"), Decimal("3"), Decimal("5"))
    row = c.to_row()
    c2 = Calculation.from_row(row)
    assert c2.operation_name == "Addition"
    assert c2.result == Decimal("5")
