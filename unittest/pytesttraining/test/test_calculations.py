import pytest
from src.calculations import Calculations


# @pytest.fixture()
# def setUp():
#     calc = Calculations()

class TestCalculations:
    calc = Calculations()

    @pytest.fixture(scope='module', autouse=True)
    def setup(self):
        pass

    @pytest.mark.parametrize("n1, n2, ex_val",
                             [(5, 5, 10), (-5, -5, -10), (0, 5, 5) ] )

    def test_add(self, n1, n2, ex_val):
        res = self.calc.add (n1, n2)
        assert res == ex_val, "error"

    def test_sub(self):
        res = self.calc.sub (10,5)
        assert res == 5, "error"

    def test_mult(self):
        res = self.calc.mult (10,5)
        assert res == 50, "error"

    def test_div(self):
        res = self.calc.div (10,5)
        assert res == 2, "error"

    @pytest.mark.skip
    def test_div_err(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(10,0)