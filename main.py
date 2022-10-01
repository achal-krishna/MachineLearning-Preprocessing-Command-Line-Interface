import os
import sys
import pandas as pd
import data_description, download, feature_scaling, imputation, categorical

if len(sys.argv) != 2:
	sys.exit("Usage: python3 main.py file.csv")

if '.csv' not in sys.argv[1]:
	sys.exit("Only csv files are accepted")

print("Welcome to the Machine Learning Preprocessing CLI!!! \U0001f600 \n")
print("Columns\n")

file = pd.read_csv(sys.argv[1])
for col in file:
	print(col, end=" ")
print("\n")

while True:
	target = input("Which is the target variable: (Press -1 to exit)  ")
	if target == '-1':
		sys.exit(0)
	yn = input("Are you sure?(y / n)  ")
	if yn.lower() == 'y':
		break
	elif yn.lower() == 'n':
		continue
	else:
		sys.exit("Invalid character")

if target not in file:
	sys.exit("This is not a valid column")

labels = file[target]
file.drop(columns=[target], inplace=True)
print("Done......")

while True:

	print("\nTasks (Preprocessing)\n")
	print("1. Data Description")
	print("2. Handling NULL Values")
	print("3. Encoding Categorical Data")
	print("4. Feature Scaling of the Dataset")
	print("5. Download the modified Dataset\n")
	task = int(input("What do you want to do? (Press -1 to exit)  "))

	if task == -1:
		sys.exit(0)
	elif task == 1:
		while True:
			print("\nTasks (Data Description) \n")
			print("1. Describe a specific Column")
			print("2. Show Properties of Each Column ")
			print("3. Show the Dataset\n")
			task = int(input("What do you want to do? (Press -1 to go back)  "))
			if task == -1:
				break
			elif task == 1:
				data_description.describe_column(file)
			elif task == 2:
				data_description.property_column(file)
			elif task == 3:
				data_description.show_dataset(file)
			else:
				print("Invalid character")
	elif task == 2:
		while True:
			print("\nImputation Tasks\n")
			print("1. Show number of Null values")
			print("2. Remove Columns ")
			print("3. Fill Null Values (With mean) ")
			print("4. Fill Null Values (With median) ")
			print("5. Fill Null Values (With mode) ")
			print("6. Show the Dataset\n")
			task = int(input("What do you want to do? (Press -1 to go back)  "))
			if task == -1:
				break
			elif task == 1:
				imputation.show_columns(file)
			elif task == 2:
				imputation.remove_columns(file)
			elif task == 3:
				imputation.fill_mean(file)
			elif task == 4:
				imputation.fill_median(file)
			elif task == 5:
				imputation.fill_mode(file)
			elif task == 6:
				imputation.show_dataset(file)
			else:
				print("Invalid character")
	elif task == 3:
		while True:
			print("\nCategorical Tasks\n")
			print("1. Show Categorical Columns")
			print("2. Performing One - Hot encoding ")
			print("3. Performing Label encoding ")
			print("4. Show the Dataset\n")
			task = int(input("What do you want to do? (Press -1 to go back)  "))
			if task == -1:
				break
			elif task == 1:
				categorical.show_categories(file)
			elif task == 2:
				categorical.one_hot(file)
			elif task == 3:
				categorical.label_encode(file)
			elif task == 4:
				categorical.show_dataset(file)
			else:
				print("Invalid character")
	elif task == 4:
		while True:
			print("\nFeature Scaling Tasks\n")
			print("1. Perform Normalization(MinMax Scaler) ")
			print("2. Perform Standardization(Standard Scaler) ")
			print("3. Show the Dataset\n")
			task = int(input("What do you want to do? (Press -1 to go back)  "))
			if task == -1:
				break
			elif task == 1:
				feature_scaling.normalize(file)
			elif task == 2:
				feature_scaling.standardize(file)
			elif task == 3:
				feature_scaling.show_dataset(file)
			else:
				print("Invalid character")
	elif task == 5:
		download.dload(file)
	else:
		print("No such task exists")

print("done")
