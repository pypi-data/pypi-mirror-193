import numpy as np
# from  scipy.special import sph_harm
from ..model          import cartesian2spherical
from pyshtools.expand import spharm_lm




def yl_i(l, Rij, SW=None, kind='real', normalization='4pi', deg=False):
	"""Compute vector of Spherical Harmonics for a set of point (ylm vector have (2l+1) components)

	Args:
		l (int)         : degree of Spherical Harmonic
		Rij (array-like): Nx3 array contain Rij of nearest neighbors compute from atom i
		SW  (array-like, optional): Nx1 values of switching function. Default to 'None'
		kind  (str, optional): kind of return result. Possible `complex`/`real`. Default to `complex`
		normalization (str, optional): '4pi', 'ortho', 'schmidt', or 'unnorm' for geodesy 4pi normalized, orthonormalized, Schmidt semi-normalized, or unnormalized spherical harmonic functions, respectively. Default to '4pi'
		deg (bool, optional): If True, theta and phi are expressed in degrees. Default to `False`

	Returns:
		yl  (array-like): vector of (2l+1) components


	???+ note

		This functions used the function `spharm_lm()` from [pyshtools](https://shtools.github.io/SHTOOLS/pyspharm_lm.html)

	???+ info "See also"

		1. [Visualizing the real forms of the spherical harmonics](https://scipython.com/blog/visualizing-the-real-forms-of-the-spherical-harmonics/)
		2. In `scipy.special.sph_harm` function the azimuthal coordinate, theta, comes before the polar coordinate, phi; anh may return complex number only

	"""
	P = cartesian2spherical(Rij)
	r,theta, phi = P[:,0], P[:,1], P[:,2]  # azimuthal coordinate is phi

	## create array to save ylm
	if kind=='complex':  # set dtype
		yl = np.zeros((2*l+1), dtype=complex)    # Ylm complex vector of (2l+1) components  ;, dtype=complex
	else:
		yl = np.zeros((2*l+1))

	Ms = np.arange(-l, l+0.1, 1, dtype=int)         #  (2l+1) values of m

	for m in Ms:
		Y = spharm_lm(l, m, theta, phi, kind=kind, normalization=normalization, degrees=deg)        # Ylm(Rij)
		## use switch function
		if SW is not None:
			yl[m] = sum(SW*Y)/ sum(SW)
		else:
			yl[m] = sum(Y)/ len(Y)

	return yl


## Old implemetation using `scipy` --> may give wrong results
	# def yl_i(l, Rij, SW=None, kind='complex'):
	# """Compute vector of Spherical Harmonics for a set of point (ylm vector have (2l+1) components)

	# Args:
	# 	l (int)         : degree of Spherical Harmonic
	# 	Rij (array-like): Nx3 array contain Rij of nearest neighbors compute from atom i
	# 	SW  (array-like, optional): Nx1 values of switching function. Default to 'None'
	# 	kind  (str, optional): form of return result. Possible `complex`/`real`. Default to `complex`

	# Returns:
	# 	yl  (array-like): vector of (2l+1) components

	# 	This functions used the function `spharm_lm()` from [pyshtools](https://shtools.github.io/SHTOOLS/pyspharm_lm.html)

	# ???+ info "See also"

	# 	1. [Visualizing the real forms of the spherical harmonics](https://scipython.com/blog/visualizing-the-real-forms-of-the-spherical-harmonics/)
	# 	2. In `scipy.special.sph_harm` function the azimuthal coordinate, theta, comes before the polar coordinate, phi; anh may return complex number only

	# """
	# P = cartesian2spherical(Rij)
	# r,theta, phi = P[:,0], P[:,1], P[:,2]  # azimuthal coordinate is phi

	# Ms = np.arange(-l, l+0.1, 1, dtype=int)         #  (2l+1) values of m
	# yl = np.zeros([Ms.shape[0]], dtype=complex)    # Ylm complex vector of (2l+1) components

	# for m in Ms:
	# 	Y = sph_harm(m, l, phi, theta)        # Ylm(Rij)  in eq.(8)

	# 	## Convert to real form: https://scipython.com/blog/visualizing-the-real-forms-of-the-spherical-harmonics/
	# 	if kind=='real':
	# 		if m < 0:
	# 			Y = np.sqrt(2) * (-1)**m * Y.imag
	# 		elif m > 0:
	# 			Y = np.sqrt(2) * (-1)**m * Y.real

	# 	## use switch function
	# 	if SW is not None:
	# 		yl[m] = sum(SW*Y)/ sum(SW)
	# 	else:
	# 		yl[m] = sum(Y)/ len(Y)

	# return yl