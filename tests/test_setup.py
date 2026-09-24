import pgmpy
import sma_bn


def test_project_imports() -> None:
    assert pgmpy is not None
    assert sma_bn is not None