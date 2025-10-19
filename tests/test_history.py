from app.history import to_dataframe
from app.calculation import Calculation
from decimal import Decimal

def test_df_conversion():
    hist = [Calculation("Addition", Decimal("1"), Decimal("2"), Decimal("3"))]
    df = to_dataframe(hist)
    assert list(df.columns) == ["operation","a","b","result","timestamp"]
    assert df.iloc[0]["operation"] == "Addition"
