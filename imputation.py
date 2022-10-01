import pandas as pd

def show_columns(file):
	print("\nNull values of each Column\n")
	print(file.isnull().sum())

def remove_columns(file):
	for col in file:
		print(col, end=" ")
	print("\n")
	while True:
		cols = input("Enter all the column(s) you want to delete (Press -1 to go back) ")
		if cols == '-1':
			return
		yn = input("Are you sure? (y / n) ")
		if yn.lower() == 'n':
			continue
		elif yn.lower() == 'y':
			break
		else:
			sys.exit("Invalid character")
	for col in cols.strip().split(" "):
		if col not in file:
			sys.exit("Invalid column")
		file.drop(columns=[col], inplace=True)
	print("Done......")

def fill_mean(file):
	for col in file:
		print(col, end=" ")
	print("\n")
	while True:
		col = input("Enter the column name (Press -1 to go back) ")
		if col == '-1':
			return
		yn = input("Are you sure? (y / n) ")
		if yn.lower() == 'n':
			continue
		elif yn.lower() == 'y':
			break
		else:
			sys.exit("Invalid character")
	if col not in file:
		sys.exit("Invalid column")
	file[col].fillna(file[col].mean(), inplace=True)
	print("Done......")

def fill_median(file):
	for col in file:
		print(col, end=" ")
	print("\n")
	while True:
		col = input("Enter the column name (Press -1 to go back) ")
		if col == '-1':
			return
		yn = input("Are you sure? (y / n) ")
		if yn.lower() == 'n':
			continue
		elif yn.lower() == 'y':
			break
		else:
			sys.exit("Invalid character")
	if col not in file:
		sys.exit("Invalid column")
	file[col].fillna(file[col].median(), inplace=True)
	print("Done......")

def fill_mode(file):
	for col in file:
		print(col, end=" ")
	print("\n")
	while True:
		col = input("Enter the column name (Press -1 to go back) ")
		if col == '-1':
			return
		yn = input("Are you sure? (y / n) ")
		if yn.lower() == 'n':
			continue
		elif yn.lower() == 'y':
			break
		else:
			sys.exit("Invalid character")
	if col not in file:
		sys.exit("Invalid column")
	file[col].fillna(file[col].mode()[0], inplace=True)
	print("Done......")

def show_dataset(file):
	n = int(input("\nHow many rows (>0) to print? (Press -1 to go back) "))
	if n == -1:
		return
	print(file.head(n))
