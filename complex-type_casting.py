# WAF that uses complex() to convert other types to complex type.
# Form-1: complex(x) -> We can use this function to convert x into complex number with real part x and imaginary part 0.
# NOTE: What converts one type value to another type is (using type casting or type coersion.) The following are inbuilt functions for type casting int(), float(), complex(), bool(), str().
complex(10)
complex(10.5) 
complex(True)
complex(False)
complex("10")
complex("10.5")
complex("ten") # Error Message
print(complex(10))
print(complex(10.5)) 
print(complex(True))
print(complex(False))
print(complex("10"))
print(complex("10.5")) 
print(float("ten")) # Error Message

# NOTE: ValueError: complex() arg is a malformed string
# Form-2: complex(x,y)
# We can use this method to convert x and y in to complex such that x will be real part and y will be imaginary part
# E.g complex(10, -2) -> 10-2j
#.    complex(True, False) -> 1+0j
