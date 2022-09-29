import numpy as np

def calculate(list):
	#convert list of 9 digits to 3x3 matrix
	if len(list) < 9:
		raise ValueError("List must contain nine numbers.")
	#data = np.array([[list]])
	#return a dictionary of calculated values
	#format: axis1, axis2, flattened
	calculations = {
		'mean': [],
		'variance': [],
		'standard deviation': [],
		'max': [],
		'min': [],
		'sum': []
	}
	
	return calculations