''' The following operators bellow are called arithmetic operators 
Arithmetic Operation
Relational Operators OR Comparison Operators
Logical Operators
Bitwise Operators
Assignment Operators
Special Operators '''
a = 10
b = 2
print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a / b =', a / b)
print('a // b =', a // b)
print('a % b =', a % b)
print('a ** b =', a ** b)

a = 10.5
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

''' Operation / always perform floating point arithmetic. Hence returning a float value.
// Can perform both floating point and integral arithmetic. If arguments are int type then the result is int type. If at least one argument is float type then result is float type.
We can use +, * operators for str type also. If we want to use + operator for str type then compulsory both arguments should be str type only otherwise we will get error.
'''

#"mangong" + 10
#print("mangong" + 10)

"mangong" + "10"
print("mangong" + "10")

''' If we use * operator for str type then compulsory one argument should be int and other argument should be str type '''
4 * "mangong"
print(4 * "mangong")

"mangong" * 4
print("mangong" * 4)

"mangong" * "mangong"
print("mangong" * "mangong")

''' + -> String Concatenation Operator
    * -> String Multiplication Operator
For any number x, x/0 and x%0 always raises "ZeroDivisionError" '''
