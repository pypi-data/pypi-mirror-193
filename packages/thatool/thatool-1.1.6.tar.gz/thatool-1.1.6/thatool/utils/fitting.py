import 	numpy  as np

def find_slope(x,y):
	"""Compute slope of a linear relation using [np.polyfit](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy.polyfit)
	See also: 'np.polyval', `np.polyder`, `np.roots`

	Args:
		x: 1d array_like
		y: 1d array_like

	Return:
		slope (float): the slope to linear relation
	"""
	## refine input

	## fitting
	params = np.polyfit(x,y,1)
	slope = params[0]
	return slope

