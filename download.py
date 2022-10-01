import pandas as pd
import sys

def dload(file):
	fname = input("Enter the FILENAME you want (Press -1 to go back) ")
	file.to_csv(f'{fname}.csv')
	print("\nHurray it is downloaded!!!\n")
	while True:
		yn = input("Do you want to exit now? (y / n) ")
		if yn.lower() == 'y':
			print("Exiting......Bye")
			sys.exit(0)
		elif yn.lower() == 'n':
			return
		else:
			print("Invalid Character\n")
