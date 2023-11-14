# WAF that uses float() to convert other type values to float
# NOTE: What converts one type value to another type is (using type casting or type coersion.) The following are inbuilt functions for type casting int(), float(), complex(), bool(), str().
float(10)
#float(10+5j)  Error Message
float(True)
float(False)
float("10")
float("10.5")
#float("ten")  Error Message
#float("0B1111")  Error Message
print(float(123.987))
#print(float(10+5j))  Error Message
print(float(True))
print(float(False))
print(float("10"))
print(float("10.5")) 
#print(float("ten"))  Error Message
#print(float("0B1111"))  Error Message

""" We can convert any type value to float type except complex type
Whenever we are trying to convert str type to float type compulsary str should be either integral or floating point literal and should be specified only in base-10
"""
