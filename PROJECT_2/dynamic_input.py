"""Reading Dynamic input from the Keyboard: In Python 2 the
- raw_input()
- input()
are available to read dynamic input from the keyboard

1) raw_input: This function always reads the data from the keyboard in the form of String Format. We have to convert that string type to our required type by using the corresponding type casting methods.E.g

x = raw_input("Enter First Number:")
print(type(x)) -> It will always print str type only for any input type
2) input(): input() function can be used to read data directly in our required format. We are not required to perform type casting."""

x = input("Enter Value")
type(x)

10
"durga"
10.5
True

"""NOTE: 
- But in Python 3 we have only input() method and raw_input() method is not available.
- Python3 input() function behavior exactly same as raw_input() method of Python2. i.e every input value is treated as str type only
- raw_input() function of Python 2 is renamed as input() function in Python 3."""


