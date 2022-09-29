import numpy as np

def calculate(list):
	#convert list of 9 digits to 3x3 matrix
	if len(list) < 9:
		raise ValueError("List must contain nine numbers.")
	data = np.array([
		list[:3],
		list[3:6],
		list[6:]
	])

	#return a dictionary of calculated values
	#format: axis1, axis2, flattened
	#entries should be normal python lists
	calculations = {
		'mean': [np.mean(data,axis=0).tolist(), np.mean(data,axis=1).tolist(), np.mean(data)],
		'variance': [np.var(data,axis=0).tolist(), np.var(data,axis=1).tolist(), np.var(data)],
		'standard deviation': [np.std(data,axis=0).tolist(), np.std(data,axis=1).tolist(), np.std(data)],
		'max': [np.amax(data,axis=0).tolist(), np.amax(data,axis=1).tolist(), np.amax(data)],
		'min': [np.min(data,axis=0).tolist(), np.min(data,axis=1).tolist(), np.min(data)],
		'sum': [np.sum(data,axis=0).tolist(), np.sum(data,axis=1).tolist(), np.sum(data)]
	}
	
	return calculations