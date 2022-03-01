"""Test the CommandFactory."""

from arithmetic_commands import AdditionCommand
from calculator_exception import CalculatorException
from command_base import PopCommand, PushCommand
from command_factory import CommandFactory
from stack import Stack


class TestCommandFactory:
    """Test Class for the CommandFactory."""

    def test_instance(self):
        """Test instanciation of CommandFactory."""
        test_stack = Stack()
        test_factory = CommandFactory(test_stack)
        assert test_factory is not None

    def test_get_registered(self):
        """
        Test get_registered.

        @return a list of registered commands.
        """
        test_stack = Stack()
        test_factory = CommandFactory(test_stack)
        assert test_factory is not None
        assert test_factory.registered == ()

    def test_register_command(self):
        """Test the register_command method."""
        test_stack = Stack()
        test_factory = CommandFactory(test_stack)
        test_factory.register(None, PushCommand)
        test_factory.register("pop", PopCommand)
        assert test_factory.registered == (None, "pop")

    def test_get_command(self):
        """Test the get_operand method."""
        test_stack = Stack()
        test_factory = CommandFactory(test_stack)
        try:
            test_factory.get_command("32")
            assert True is False
        except CalculatorException as ex:
            assert str(ex) == "CalculatorException: >>>command (32) not " + \
                              "registered and no default set<<<"
        test_factory.register(None, PushCommand)
        test_factory.get_command("32").run()
        test_factory.get_command("11").run()
        assert len(test_stack) == 2
        test_factory.register("+", AdditionCommand)
        test_factory.get_command("+").run()
        assert len(test_stack) == 1
        assert test_stack.pop() == 43
