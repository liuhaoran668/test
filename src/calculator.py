"""示例模块：提供基本的数学运算功能。"""

from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    将两个数字相加。

    Args:
        a: 第一个数字
        b: 第二个数字

    Returns:
        两个数字的和

    Examples:
        >>> add(2, 3)
        5
        >>> add(2.5, 3.5)
        6.0
    """
    return a + b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    将两个数字相乘。

    Args:
        a: 第一个数字
        b: 第二个数字

    Returns:
        两个数字的乘积

    Examples:
        >>> multiply(2, 3)
        6
        >>> multiply(2.5, 4)
        10.0
    """
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """
    将第一个数字除以第二个数字。

    Args:
        a: 被除数
        b: 除数

    Returns:
        除法结果

    Raises:
        ValueError: 当除数为零时

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(10, 0)
        Traceback (most recent call last):
        ...
        ValueError: 除数不能为零
    """
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


class Calculator:
    """简单的计算器类。"""

    def __init__(self) -> None:
        """初始化计算器。"""
        self.result: Union[int, float] = 0

    def reset(self) -> None:
        """重置计算器结果为 0。"""
        self.result = 0

    def add(self, value: Union[int, float]) -> "Calculator":
        """
        将值加到当前结果。

        Args:
            value: 要添加的值

        Returns:
            Calculator 实例（用于链式调用）
        """
        self.result += value
        return self

    def get_result(self) -> Union[int, float]:
        """
        获取当前结果。

        Returns:
            当前计算结果
        """
        return self.result
