from typing import Callable, NotRequired, Optional, TypedDict
from talon import Module, actions

mod = Module()

mod.tag("code_operators_array", desc="Tag for enabling array operator commands")
mod.tag("code_operators_assignment", desc="Tag for enabling assignment commands")
mod.tag("code_operators_bitwise", desc="Tag for enabling bitwise operator commands")
mod.tag(
    "code_operators_lambda", desc="Tag for enabling commands for anonymous functions"
)
mod.tag("code_operators_math", desc="Tag for enabling mathematical operator commands")
mod.tag("code_operators_pointer", desc="Tag for enabling pointer operator commands")

mod.list("code_operators_array", desc="List of code operators for arrays")
mod.list("code_operators_assignment", desc="List of code operators for assignments")
mod.list("code_operators_bitwise", desc="List of code operators for bitwise operations")
mod.list("code_operators_lambda", desc="List of code operators for anonymous functions")
mod.list(
    "code_operators_math", desc="List of code operators for mathematical operations"
)
mod.list("code_operators_pointer", desc="List of code operators for pointers")


Operator = str | Callable[[], None]


class Operators(TypedDict):
    # code_operators_array
    SUBSCRIPT: NotRequired[Operator]

    # code_operators_assignment
    ASSIGNMENT: NotRequired[Operator]
    ASSIGNMENT_OR: NotRequired[Operator]
    ASSIGNMENT_SUBTRACTION: NotRequired[Operator]
    ASSIGNMENT_ADDITION: NotRequired[Operator]
    ASSIGNMENT_MULTIPLICATION: NotRequired[Operator]
    ASSIGNMENT_DIVISION: NotRequired[Operator]
    ASSIGNMENT_MODULO: NotRequired[Operator]
    ASSIGNMENT_INCREMENT: NotRequired[Operator]
    ASSIGNMENT_BITWISE_AND: NotRequired[Operator]
    ASSIGNMENT_BITWISE_OR: NotRequired[Operator]
    ASSIGNMENT_BITWISE_EXCLUSIVE_OR: NotRequired[Operator]
    ASSIGNMENT_BITWISE_LEFT_SHIFT: NotRequired[Operator]
    ASSIGNMENT_BITWISE_RIGHT_SHIFT: NotRequired[Operator]

    # code_operators_bitwise
    BITWISE_AND: NotRequired[Operator]
    BITWISE_OR: NotRequired[Operator]
    BITWISE_NOT: NotRequired[Operator]
    BITWISE_EXCLUSIVE_OR: NotRequired[Operator]
    BITWISE_LEFT_SHIFT: NotRequired[Operator]
    BITWISE_RIGHT_SHIFT: NotRequired[Operator]

    # code_operators_lambda
    LAMBDA: NotRequired[Operator]

    # code_operators_math
    MATH_SUBTRACT: NotRequired[Operator]
    MATH_ADD: NotRequired[Operator]
    MATH_MULTIPLY: NotRequired[Operator]
    MATH_DIVIDE: NotRequired[Operator]
    MATH_MODULO: NotRequired[Operator]
    MATH_EXPONENT: NotRequired[Operator]
    MATH_EQUAL: NotRequired[Operator]
    MATH_NOT_EQUAL: NotRequired[Operator]
    MATH_GREATER_THAN: NotRequired[Operator]
    MATH_GREATER_THAN_OR_EQUAL_TO: NotRequired[Operator]
    MATH_LESS_THAN: NotRequired[Operator]
    MATH_LESS_THAN_OR_EQUAL_TO: NotRequired[Operator]
    MATH_AND: NotRequired[Operator]
    MATH_OR: NotRequired[Operator]
    MATH_NOT: NotRequired[Operator]
    MATH_IN: NotRequired[Operator]
    MATH_NOT_IN: NotRequired[Operator]

    # code_operators_pointer
    POINTER_INDIRECTION: NotRequired[Operator]
    POINTER_ADDRESS_OF: NotRequired[Operator]
    POINTER_STRUCTURE_DEREFERENCE: NotRequired[Operator]


@mod.action_class
class Actions:
    def code_operator(id: str):
        """Insert a code operator"""
        operators: Operators = actions.user.code_get_operators()

        # This language has not implement the get operators and we therefore use the fallback
        if operators is None:
            operators_fallback(id)
            return

        operator = operators.get(id)

        if operator is None:
            raise ValueError(f"Operator {id} not found")

        if type(operator) is str:
            actions.insert(operator)
        else:
            operator()

    def code_get_operators() -> Optional[Operators]:
        """Get code operators dictionary"""
        return None


# Fallback is to rely on the legacy actions
def operators_fallback(id: str) -> None:
    match id:
        # code_operators_array
        case "subscript":
            actions.user.code_operator_subscript()

        # code_operators_assignment
        case "ASSIGNMENT":
            actions.user.code_operator_assignment()
        case "ASSIGNMENT_OR":
            actions.user.code_or_operator_assignment()
        case "ASSIGNMENT_SUBTRACTION":
            actions.user.code_operator_subtraction_assignment()
        case "ASSIGNMENT_ADDITION":
            actions.user.code_operator_addition_assignment()
        case "ASSIGNMENT_MULTIPLICATION":
            actions.user.code_operator_multiplication_assignment()
        case "ASSIGNMENT_MODULO":
            actions.user.code_operator_modulo_assignment()
        case "ASSIGNMENT_INCREMENT":
            actions.user.code_operator_increment()
        case "ASSIGNMENT_BITWISE_AND":
            actions.user.code_operator_bitwise_and_assignment()
        case "ASSIGNMENT_BITWISE_OR":
            actions.user.code_operator_bitwise_or_assignment()
        case "ASSIGNMENT_BITWISE_EXCLUSIVE_OR":
            actions.user.code_operator_bitwise_exclusive_or_assignment()
        case "ASSIGNMENT_BITWISE_LEFT_SHIFT":
            actions.user.code_operator_bitwise_left_shift_assignment()
        case "ASSIGNMENT_BITWISE_RIGHT_SHIFT":
            actions.user.code_operator_bitwise_right_shift_assignment()

        # code_operators_bitwise
        case "BITWISE_AND":
            actions.user.code_operator_bitwise_and()
        case "BITWISE_OR":
            actions.user.code_operator_bitwise_or()
        case "BITWISE_NOT":
            actions.user.code_operator_bitwise_not()
        case "BITWISE_EXCLUSIVE_OR":
            actions.user.code_operator_bitwise_exclusive_or()
        case "BITWISE_LEFT_SHIFT":
            actions.user.code_operator_bitwise_left_shift()
        case "BITWISE_RIGHT_SHIFT":
            actions.user.code_operator_bitwise_right_shift()

        # code_operators_lambda
        case "LAMBDA":
            actions.user.code_operator_lambda()

        # code_operators_math
        case "MATH_SUBTRACT":
            actions.user.code_operator_subtraction()
        case "MATH_ADD":
            actions.user.code_operator_addition()
        case "MATH_MULTIPLY":
            actions.user.code_operator_multiplication()
        case "MATH_DIVIDE":
            actions.user.code_operator_division()
        case "MATH_MODULO":
            actions.user.code_operator_modulo()
        case "MATH_EXPONENT":
            actions.user.code_operator_exponent()
        case "MATH_EQUAL":
            actions.user.code_operator_equal()
        case "MATH_NOT_EQUAL":
            actions.user.code_operator_not_equal()
        case "MATH_GREATER_THAN":
            actions.user.code_operator_greater_than()
        case "MATH_GREATER_THAN_OR_EQUAL_TO":
            actions.user.code_operator_greater_than_or_equal_to()
        case "MATH_LESS_THAN":
            actions.user.code_operator_less_than()
        case "MATH_LESS_THAN_OR_EQUAL_TO":
            actions.user.code_operator_less_than_or_equal_to()
        case "MATH_AND":
            actions.user.code_operator_and()
        case "MATH_OR":
            actions.user.code_operator_or()
        case "MATH_NOT":
            actions.user.code_operator_not()
        case "MATH_IN":
            actions.user.code_operator_in()
        case "MATH_NOT_IN":
            actions.user.code_operator_not_in()

        # code_operators_pointer
        case "POINTER_INDIRECTION":
            actions.user.code_operator_indirection()
        case "POINTER_ADDRESS_OF":
            actions.user.code_operator_address_of()
        case "POINTER_STRUCTURE_DEREFERENCE":
            actions.user.code_operator_structure_dereference()

        case _:
            raise ValueError(f"Operator {id} not found")
