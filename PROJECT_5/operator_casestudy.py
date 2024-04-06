# Slice Operator Case Study:
s = 'abcdefghij'
s[1:6:2]
s[::1]
s[::-1]
s[3:7:-1]
s[7:4:-1]
s[0:10000:1]
s[-4:1:-1]
s[-4:1:-2]
s[5:0:1]
#s[9:0:0]
s[0:-10:-1]
s[0:-11:-1]
s[0:0:1]
s[0:-9:-2]
s[-5:-9:-2]
s[10:-1:-1]
s[10000:2:-1]

# NOTE: Slice operator never raises IndexError
