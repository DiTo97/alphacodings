import pathlib

import pytest


ROOT = pathlib.Path(__file__).resolve().parents[1]
examples_dir = ROOT / "examples"


@pytest.fixture(scope="session")
def benchmark() -> str:
    benchmark = examples_dir / "benchmark.html"

    with benchmark.open("rt", encoding="utf-8") as f:
        string = f.read()

    return string
