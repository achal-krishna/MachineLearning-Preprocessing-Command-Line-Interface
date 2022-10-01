import pandas as pd

def describe_column(file):
	for col in file:
		print(col, end=" ")
	print("\n")
	column = input("Which Column?  ")
	if column not in file:
		sys.exit("Invalid column")
	print(file[column].describe())

def property_column(file):
	print(file.describe(), "\n")
	print(file.info(), "\n")
	# print(file.isnull().sum().sum())

def show_dataset(file):
	n = int(input("\nHow many rows (>0) to print? (Press -1 to go back) "))
	if n == -1:
		return
	print(file.head(n))
