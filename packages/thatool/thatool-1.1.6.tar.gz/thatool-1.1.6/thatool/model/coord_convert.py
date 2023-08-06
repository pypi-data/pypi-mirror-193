import numpy as np


def cartesian2spherical(xyz):
	"""Convert cartesian coordinates to [Spherical coordinates](https://en.wikipedia.org/wiki/Spherical_coordinate_system)

	Args:
		xyz (array): Mx3 array contain Cartesian coordinates (X, Y, Z)

	Returns:
		shpCoord (array): Mx3 array contain Spherical coordinates (R, theta, phi). Also (radial distance, polar angle, azimuthal(longitude) angle)


	!!! note

		1. The polar(theta) angle defined from from Z-axis down (zero at the North pole to 180° at the South pole)
		2. adapted from [this](https://stackoverflow.com/questions/4116658/faster-numpy-cartesian-to-spherical-coordinate-conversion)

	!!! info

		There are many conventions that angles can be
		- In geography, angles are in latitude/longitude or elevation/azimuthal form, polar angle is called [`latitude`](https://en.wikipedia.org/wiki/Latitude), measuze from XY-plane (ranges from -90° at the south pole to 90° at the north pole, with 0° at the Equator)

		![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Latitude_and_longitude_graticule_on_an_ellipsoid.svg/200px-Latitude_and_longitude_graticule_on_an_ellipsoid.svg.png)

		- In mathematics and physics, polar angle measured from Z-axis (zero at the North pole to 180° at the South pole)

		![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/3D_Spherical.svg/360px-3D_Spherical.svg.png)

		- In `scipy`, polar angle is defined as [Colatitude](https://en.wikipedia.org/wiki/Colatitude), which is a non-negative quantity, ranging from zero at the North pole to 180° at the South pole (same as commonly used in mathematics and physics)
	"""
	x, y, z = xyz[:,0], xyz[:,1], xyz[:,2]

	r       =  np.sqrt(x**2 + y**2 + z**2)
	theta   = np.arctan2(np.sqrt(x**2 + y**2), z) # for elevation angle defined from Z-axis down
	# theta   = np.arctan2(z, np.sqrt(x**2 + y**2)) # for elevation angle defined from XY-plane up
	phi     =  np.arctan2(y,x)

	return np.column_stack((r, theta, phi))
