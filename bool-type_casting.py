# WAF that uses bool() to convert other type values to bool type.
# NOTE: What converts one type value to another type is (using type casting or type coersion.) The following are inbuilt functions for type casting int(), float(), complex(), bool(), str().
bool(0)
bool(1) 
bool(10)
bool(10.5)
bool(0.178)
bool(0.0)
bool(10-2j) 
bool(0+1.5j)
bool(0+0j) 
bool("True")
bool("False")
bool("")
print(bool(0))
print(bool(1)) 
print(bool(10))
print(bool(10.5))
print(bool(0.178))
print(bool(0.0)) 
print(bool(10-2j))
print(bool(0+1.5j))
print(bool(0+0j))
print(bool("True"))
print(bool("False"))
print(bool(""))

