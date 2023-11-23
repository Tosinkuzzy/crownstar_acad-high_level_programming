""" A simple program illustrating chaotic behaviour."""
def main():
	print("This program illustrates a chaotic function")
	x = eval(input("Enter a number between 0s and 1s: "))
	for i in range(10):
		x = 3.9 * x * (1 - x)
		print(x)
main()
