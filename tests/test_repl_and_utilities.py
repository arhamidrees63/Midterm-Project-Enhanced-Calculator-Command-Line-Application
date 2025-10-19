import io
import sys
import pytest
from decimal import Decimal
from app.calculator import Calculator
from app.calculator_repl import calculator_repl
from app.input_validators import to_decimal, ValidationError
from app.history import to_dataframe, save_history, load_history
from app.calculation import Calculation
import pandas as pd
import os


def test_input_validator_valid():
    assert to_decimal("5") == Decimal("5")
    assert to_decimal("3.14") == Decimal("3.14")


def test_input_validator_invalid():
    with pytest.raises(ValidationError):
        to_decimal("abc")
    with pytest.raises(ValidationError):
        to_decimal("9999999999999999999999999999999999999999999999", max_value=100)


def test_history_save_and_load(tmp_path):
    # prepare dummy history
    calc = Calculation("Addition", Decimal("1"), Decimal("2"), Decimal("3"))
    hist = [calc]

    file_path = tmp_path / "history.csv"
    save_history(hist, file_path)

    assert file_path.exists()

    loaded = load_history(file_path)
    assert len(loaded) == 1
    assert loaded[0].operation == "Addition"
    assert loaded[0].result == Decimal("3")


def test_to_dataframe_conversion():
    hist = [Calculation("Add", Decimal("1"), Decimal("2"), Decimal("3"))]
    df = to_dataframe(hist)
    assert isinstance(df, pd.DataFrame)
    assert "operation" in df.columns


def test_repl_help_command(monkeypatch, capsys):
    inputs = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    try:
        calculator_repl()
    except SystemExit:
        pass
    out = capsys.readouterr().out
    assert "Available Commands" in out


def test_repl_add_command(monkeypatch, capsys):
    inputs = iter(["add 2 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    try:
        calculator_repl()
    except SystemExit:
        pass
    output = capsys.readouterr().out
    assert "5" in output

