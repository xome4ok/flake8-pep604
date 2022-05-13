import pytest

from flake8_pep604 import PEP604Checker


class TestZQ002:
    @pytest.mark.parametrize(("checker", "expected_errors"), [("zq002_1.py", 9), ("zq002_2.py", 9)], indirect=["checker"])
    def test_it_finds_optional(self, checker: PEP604Checker, expected_errors: int) -> None:
        result = checker.run()
        errors = list(result)
        assert len(errors) == expected_errors
        assert all(e[2].startswith("ZQ002") for e in errors)

