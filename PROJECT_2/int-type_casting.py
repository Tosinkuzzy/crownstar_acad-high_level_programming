# WAF to convert values from other types to int.
# NOTE: What converts one type value to another type is (using type casting or type coersion.) The following are inbuilt functions for type casting int(), float(), complex(), bool(), str()
int(123.987)
#int(10+5j)
int(True)
int(False)
int("10")
int("10.5")
int("ten")
int("0B1111")
print(int(123.987))
print(int(10+5j)) # Error Message
print(int(True))
print(int(False))
print(int("10"))
print(int("10.5")) # Error Message
print(int("ten")) # Error Message
print(int("0B1111")) # Error Message

# The errors above generate from the fact that we can convert from any type to int except complex type
# If we want to convert str type to int type, compulsary str should contain only integral value and should be specified in base-10
