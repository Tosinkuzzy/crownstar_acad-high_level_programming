"""Operator Precedence. Which operators will be evaluated first if multiple operators are present."""

#E.g 
print(3 + 10 * 2)
print((3 + 10) * 2)

""" The followint lists describes operator precedence in Python.
() -> Parenthesis
** -> Exponential Operator
~, - -> Bitwise Complement Operator, Unary Minus Operator
*, /, %, // -> Multiplication, Division, Modulo, Floor Division
+, - -> Addition, Subtraction
<<, >> -> Left and Right Shift
& -> Bitwise And
^ -> Bitwise X - OR
| -> Bitwise OR
>, >=, <, <=, ==, != -> Relational OR Comparison Operators
=, +=, -=, *=... -> Assignment Operators
is, is not -> Identity Operators
in, not in -> Membership Operators
not -> Logical not
and -> Logical and
or -> Logical or
"""

a = 30
b = 20
c = 10
d = 5
print((a + b) * c / d)
print((a + b) * (c / d))
print(a + (b * c) / d)

print(3 / 2 * 4 + 3 + (10 / 5) ** 3 - 2)
print(3 / 2 * 4 + 3 + 2.0 ** 3 - 2)
print(3 / 2 * 4 + 3 + 8.0 - 2)
print(1.5 * 4 + 3 + 8.0 - 2)
print(15.0)

