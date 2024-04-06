#!/usr/bin/env Python3

""" Accessing Characters by using slice Operator:
- Syntax: s[bEginindex:endindex:step]
- Begin Index: From where we have to consider slice (substring)
- End Index: We have to terminate the slice (substring) at endindex-1
- Step: Incremented Value

NOTE:
- If we are not specifying bEgin index then it will consider from bEginning of the string.
- If we are not specifying end index then it will consider up to end of the string.
- The default value for step is 1."""

s = "Learning Python is very very easy!!!"
s[1:7:1]
'earnin'
s[1:7]
'earnin'
s[1:7:2]
'eri'
s[:7]
'Learnin'
s[7:]
'g Python is very very easy!!!'
s[::]
'Learning Python is very very easy!!!'
s[:]
'Learning Python is very very easy!!!'
s[::-1]
'!!!ysae yrev yrev si nohtyP gninraeL'

""" Behaviour of Slice Operator:
- s[bEgin:end:step]
- Step value can be either +ve or -ve
- If +ve then it should be forward direction(left to right) and we have to consider bEgin to end-1
- If -ve then it should be backward direction(right to left) and we have to consider to end+1

NOTE:
- In the backward direction if end value is -1 then result is always empty
- In the forward direction if end value is 0 then result is always empty.

In Forward Direction:
- default value for bEgin: 0
- default value for end: length of string
- default value for step: +1

In Backward Direction:
- default value for bEgin: -1
- default value for end: -(length of string+1)

NOTE: Either forward or backward direction, we can take both +ve and -ve values for bEgin and end index."""

