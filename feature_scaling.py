import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

def normalize(file):
	sc = MinMaxScaler()
	while True:
			print("\nNormalization Tasks\n")
			print("1. Normalize a specific column ")
			print("2. Normalize the whole Dataset ")
			print("3. Show the Dataset\n")
			task = int(input("What do you want to do? (Press -1 to go back)  "))
			flag = 0
			if task == -1:
				break
			elif task == 1:
				print(file.describe())
				print("\n")
				cols = input("Enter all the column(s) you want to normalize (Press -1 to go back) ")
				if cols == '-1':
					break
				for col in cols.strip().split(" "):
					if col in file:
						arr = np.array(file[col])
						arr = arr.reshape(arr.shape[0], 1)
						file[col] = pd.DataFrame(sc.fit_transform(arr))
					else:
						print("Invalid Column")
						flag = 1
						break
				if flag == 0:
					print("Normalizing Done ......")
			elif task == 2:
				for col in file:
					arr = np.array(file[col])
					arr = arr.reshape(arr.shape[0], 1)
					file[col] = pd.DataFrame(sc.fit_transform(arr))
				print("Normalizing Done ......")
			elif task == 3:
				show_dataset(file)
			else:
				print("Invalid character")

def standardize(file):
	sc = StandardScaler()
	while True:
			print("\nStandardization Tasks\n")
			print("1. Standardize a specific column ")
			print("2. Standardize the whole Dataset ")
			print("3. Show the Dataset\n")
			task = int(input("What do you want to do? (Press -1 to go back)  "))
			flag = 0
			if task == -1:
				break
			elif task == 1:
				print(file.describe())
				print("\n")
				cols = input("Enter all the column(s) you want to standardize (Press -1 to go back) ")
				if cols == '-1':
					break
				for col in cols.strip().split(" "):
					if col in file:
						arr = np.array(file[col])
						arr = arr.reshape(arr.shape[0], 1)
						file[col] = pd.DataFrame(sc.fit_transform(arr))
					else:
						print("Invalid Column")
						flag =1
						break
				if flag == 0:
					print("Standardizing Done ......")
			elif task == 2:
				for col in file:
					arr = np.array(file[col])
					arr = arr.reshape(arr.shape[0], 1)
					file[col] = pd.DataFrame(sc.fit_transform(arr))
				print("Standardizing Done ......")
			elif task == 3:
				show_dataset(file)
			else:
				print("Invalid character")

def show_dataset(file):
	n = int(input("\nHow many rows (>0) to print? (Press -1 to go back) "))
	if n == -1:
		return
	print(file.head(n))
