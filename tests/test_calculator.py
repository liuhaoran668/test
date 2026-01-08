"""测试计算器模块。"""

import pytest

from src.calculator import Calculator, add, divide, multiply


class TestBasicOperations:
    """测试基本数学运算。"""

    def test_add_integers(self) -> None:
        """测试整数相加。"""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0

    def test_add_floats(self) -> None:
        """测试浮点数相加。"""
        assert add(2.5, 3.5) == 6.0
        assert add(1.1, 2.2) == pytest.approx(3.3)

    def test_multiply(self) -> None:
        """测试乘法运算。"""
        assert multiply(2, 3) == 6
        assert multiply(-2, 3) == -6
        assert multiply(2.5, 4) == 10.0

    def test_divide(self) -> None:
        """测试除法运算。"""
        assert divide(10, 2) == 5.0
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self) -> None:
        """测试除以零的情况。"""
        with pytest.raises(ValueError, match="除数不能为零"):
            divide(10, 0)


class TestCalculator:
    """测试计算器类。"""

    def test_calculator_init(self) -> None:
        """测试计算器初始化。"""
        calc = Calculator()
        assert calc.get_result() == 0

    def test_calculator_add(self) -> None:
        """测试计算器加法。"""
        calc = Calculator()
        calc.add(5).add(3)
        assert calc.get_result() == 8

    def test_calculator_reset(self) -> None:
        """测试计算器重置。"""
        calc = Calculator()
        calc.add(10)
        calc.reset()
        assert calc.get_result() == 0

    def test_calculator_chaining(self) -> None:
        """测试计算器链式调用。"""
        calc = Calculator()
        result = calc.add(1).add(2).add(3).get_result()
        assert result == 6
