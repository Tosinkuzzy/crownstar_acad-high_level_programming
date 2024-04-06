#!/usr/bin/env python3

# Slice Operator Case Study:
s = 'abcdefghij'
print(s[1:6:2])
print(s[::1])
print(s[::-1])
print(s[3:7:-1])
print(s[7:4:-1])
print(s[0:10000:1])
print(s[-4:1:-1])
print(s[-4:1:-2])
print(s[5:0:1])
#s[9:0:0]
print(s[0:-10:-1])
print(s[0:-11:-1])
print(s[0:0:1])
print(s[0:-9:-2])
print(s[-5:-9:-2])
print(s[10:-1:-1])
print(s[10000:2:-1])

# NOTE: Slice operator never raises IndexError
