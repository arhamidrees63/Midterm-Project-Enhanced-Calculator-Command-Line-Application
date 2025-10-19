from decimal import Decimal
import pytest
from app.operations import OperationFactory, OperationError

@pytest.mark.parametrize("op,a,b,expected", [
    ("add","2","3", Decimal("5")),
    ("subtract","7","2", Decimal("5")),
    ("multiply","3","4", Decimal("12")),
    ("divide","8","2", Decimal("4")),
    ("power","2","3", Decimal("8")),
    ("root","9","2", Decimal("3")),
    ("modulus","7","3", Decimal("1")),
    ("int_divide","7","3", Decimal("2")),
    ("percent","50","200", Decimal("25")),
    ("abs_diff","-2","5", Decimal("7")),
])
def test_ops(op, a, b, expected):
    opi = OperationFactory.create_operation(op)
    res = opi.execute(Decimal(a), Decimal(b))
    assert res == expected

def test_divide_by_zero():
    opi = OperationFactory.create_operation("divide")
    with pytest.raises(OperationError):
        opi.execute(Decimal("1"), Decimal("0"))
