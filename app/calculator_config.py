from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv(override=True)

@dataclass(frozen=True)
class CalculatorConfig:
    log_dir: Path
    history_dir: Path
    max_history_size: int
    auto_save: bool
    precision: int
    max_input_value: float
    default_encoding: str

    @staticmethod
    def load():
        return CalculatorConfig(
            log_dir=Path(os.getenv("CALCULATOR_LOG_DIR", "logs")),
            history_dir=Path(os.getenv("CALCULATOR_HISTORY_DIR", "data")),
            max_history_size=int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "1000")),
            auto_save=os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true",
            precision=int(os.getenv("CALCULATOR_PRECISION", "10")),
            max_input_value=float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", "1e12")),
            default_encoding=os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8"),
        )
