import pandas as pd
from sklearn.preprocessing import LabelEncoder

def show_categories(file):
	print("Categorical Column 	 Unique Values ")
	for col in file:
		if file[col].dtype == 'object':
			spaces = (16 - len(col)) * " "
			print(f'{col}{spaces} 	 {file[col].describe()[1]}')
	print("\n")

def one_hot(file):
	print("Categorical Column 	 Unique Values ")
	for col in file:
		if file[col].dtype == 'object':
			spaces = (16 - len(col)) * " "
			print(f'{col}{spaces} 	 {file[col].describe()[1]}')

	while True:
		col = input("\nWhich column would you like to one - hot encode? (Press -1 to go back) ")
		if col == '-1':
			return
		elif col in file:
			new_cols = pd.get_dummies(file[col])
			file.drop(col, axis=1, inplace=True)
			for col in new_cols:
				file[col] = new_cols[col]
			print("Encoding Done......")
			while True:
				yn = input("Are there more columns to be encoded? (y / n) ")
				if yn.lower() == 'y':
					break
				elif yn.lower() == 'n':
					return
				else:
					print("Invalid character")
		else:
			print("Invalid column")
			continue

def label_encode(file):
	le = LabelEncoder()
	print("Categorical Column 	 Unique Values ")
	for col in file:
		if file[col].dtype == 'object':
			spaces = (16 - len(col)) * " "
			print(f'{col}{spaces} 	 {file[col].describe()[1]}')

	while True:
		col = input("\nWhich column would you like to label encode? (Press -1 to go back) ")
		if col == '-1':
			return
		elif col in file:
			file[col] = le.fit_transform(file[col])
			print("Encoding Done......")
			while True:
				yn = input("Are there more columns to be encoded? (y / n) ")
				if yn.lower() == 'y':
					break
				elif yn.lower() == 'n':
					return
				else:
					print("Invalid character")
		else:
			print("Invalid column")
			continue

def show_dataset(file):
	n = int(input("\nHow many rows (>0) to print? (Press -1 to go back) "))
	if n == -1:
		return
	print(file.head(n))
