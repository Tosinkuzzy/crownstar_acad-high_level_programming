"""
*********
***
*********
*****
****************
*******
"""
# A program to print month after user input.

def main():
	print("Months Jan to Dec:")
	print("Pick 1 to 12: ")
	m = int(input("Birthday Month: "))
	osu = {1:"January", 2:"Feburary", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
	type(osu)
	m_os = osu
	print("Birthday month is " + m_os[m])
#.zfill(2)])

#if __name__ == "__main__":
main()
