from app.calculator import Calculator
from app.operations import OperationFactory
from decimal import Decimal
import os

def test_basic_flow(tmp_path, monkeypatch):
    # point config dirs via env
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("CALCULATOR_LOG_DIR", str(tmp_path / "logs"))
    calc = Calculator()

    # run op
    calc.set_operation(OperationFactory.create_operation("add"))
    r = calc.perform_operation("2","3")
    assert r == Decimal("5")
    assert "Addition(2, 3) = 5" in calc.show_history()[0]

    # undo/redo
    assert calc.undo() is True
    assert calc.show_history() == []
    assert calc.redo() is True
    assert len(calc.show_history()) == 1

    # save/load
    calc.save_history()
    assert (tmp_path / "data" / "history.csv").exists()
    calc.clear_history()
    assert calc.show_history() == []
    calc.load_history()
    assert len(calc.show_history()) == 1
