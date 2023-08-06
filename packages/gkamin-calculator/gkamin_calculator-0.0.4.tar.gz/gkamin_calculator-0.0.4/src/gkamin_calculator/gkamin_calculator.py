from typing import Optional


class Calculator:

    def __init__(self, init_value: Optional[float] = None):
        """
        This is a calculator that performs basic functions and
        stores the last result in memory. Initial value can be entered
        by using optional input parameter, otherwise it is equal to zero.

        :param init_value: optionally entered an initial value.
        """

        if init_value:
            self.result = init_value
        else:
            self.result = 0  # initial result value equals to zero.

    def add(self, addend: float) -> float:
        """
        Method to add input value to last stored result.
        Initially to 0.

        :param addend: input value that is added.
        :return: addition result.
        """

        self.result += addend

        return self.result

    def subtract(self, subtrahend: float) -> float:
        """
        Method to subtract input value from last stored result.
        Initially from 0.

        :param subtrahend: input value that is subtracted.
        :return: subtraction result.
        """

        self.result -= subtrahend

        return self.result

    def multiply(self, multiplier: float) -> float:
        """
        Method to multiply input value by last stored result.
        Initially by 0.

        :param multiplier: input value by which is multiplied.
        :return: multiplication result.
        """

        self.result *= multiplier

        return self.result

    def divide(self, divisor: float) -> float:
        """
        Method to divide last stored result by input value.
        Initially dividend is equal 0.

        :param divisor: input value by which is divided.
        :return: division result.
        """

        self.result /= divisor

        return self.result

    def root(self, degree_of_root: float, radicand: Optional[float] = None) -> float:
        """
        Method to extract n-th root from last stored result, where n is degree of root.
        If this is the first operation performed (initially radicand is equal to 0),
        optional input value to be used to set required radicand value.

        :param degree_of_root: degree of root.
        :param radicand: optional inout value to take the root of.
        :return: result of an n-th root.
        """

        if not radicand:  # when only 1st parameter is entered.
            self.result = self.result ** (1 / degree_of_root)
        else:
            self.result = radicand ** (1 / degree_of_root)  # when this is the 1st operation performed.

        return self.result

    def reset(self):
        """
        Method to reset the last stored result to zero.
        :return: initial result value
        """

        self.result = 0

        return self.result
