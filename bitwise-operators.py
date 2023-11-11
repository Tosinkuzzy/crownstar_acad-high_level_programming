''' Bitwise Operators: These operators are only applicable for int and boolean types. By mistake, if we are trying to apply for any other type then we will get Error.
&, |, ^, ~, <<, >> '''
print(4 & 5)
#print(10.5 & 5.6)
print(True & True)

''' & -> If both bits are 1 then only result is 1 otherwise result is 0
| -> If atlease one bit is 1 then result is 1 otherwise result is 0
^ -> If bits are different then only result is 1 otherwise result is 0
~ -> Bitwise complement operator
1 -> 0 & 0 -> 1
<< -> Bitwise Left Shift
>> -> Bitwise Right Shift
'''
print(4 & 5)
print(4 | 5)
print(4 ^ 5)

''' Bitwise Complement Operator (~): We have to apply complement for total bits '''
print(~5)

''' NOTE: 
a) The most significant bit acts as sign bit. 0 value represents +ve number where as 1 represents -ve value.
b) Positive numbers will be represented directly in the memory where as -ve numbers will be represented indirectly in 2's complement form. '''
