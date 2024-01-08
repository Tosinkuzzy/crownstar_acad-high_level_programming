""" LOOPS WITH ELSE BLOCK:
- Inside loop execution, if break statement is not executed, then only else part will be executed.
- else means loop without break."""

cart=[10, 20, 30, 40, 50]
for item in cart:
    if item>=500:
        print("We cannot process this order")
        break
    print(item)
else:
        print("Congrats ...all items processed successfully")
        
# E.g:

cart=[10, 20, 600, 30, 40, 50]
for item in cart:
    if item>=500:
        print("We cannot process this order")
        break
    print(item)
else:
    print("Congrats ...all items processed successfully")
